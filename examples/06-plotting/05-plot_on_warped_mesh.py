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
.. _plot_on_warped_mesh:

Warp the mesh by a field for plotting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to warp the mesh by a vector field,
enabling to plot on the deformed geometry.

"""

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

# Get and show the initial model
model = dpf.Model(examples.find_multishells_rst())
print(model)
model.plot(title="Model", text="Model.plot()")

# Define a scaling factor and a step for the field to be used for warping.
scale_factor = 0.001
step = 1

# Define a result to deform by
disp_result = model.results.displacement.on_time_scoping([step])
disp_op = disp_result()
# Get the displacement field
disp_fc = disp_result.eval()
disp_field = disp_fc[0]

# Get the mesh and plot it as a deformed geometry using a Result, an Operator,
# a Field or a FieldsContainer
mesh = model.metadata.meshed_region
mesh.plot(
    deform_by=disp_result,
    scale_factor=scale_factor,
    title="MeshedRegion",
    text="MeshedRegion.plot()",
)
# mesh.plot(deform_by=disp_op, scale_factor=scale_factor,
#           title='MeshedRegion', text='MeshedRegion.plot()')
# mesh.plot(deform_by=disp_fc, scale_factor=scale_factor,
#           title='MeshedRegion', text='MeshedRegion.plot()')
# mesh.plot(deform_by=disp_field, scale_factor=scale_factor,
#           title='MeshedRegion', text='MeshedRegion.plot()')

# Plot the displacement field on the deformed geometry directly
disp_field.plot(
    deform_by=disp_result, scale_factor=scale_factor, title="Field", text="Field.plot()"
)
# or by applying it to the mesh
mesh.plot(
    disp_field,
    deform_by=disp_result,
    scale_factor=scale_factor,
    title="MeshedRegion",
    text="MeshedRegion.plot(disp_field)",
)

# Split the model by material and plot the deformed MeshesContainer obtained
split_mesh_op = dpf.operators.mesh.split_mesh(mesh=mesh, property="mat")
meshes_cont = split_mesh_op.get_output(0, dpf.types.meshes_container)
meshes_cont.plot(
    deform_by=disp_result,
    scale_factor=scale_factor,
    title="MeshesContainer",
    text="MeshesContainer.plot()",
)

# Create a corresponding FieldsContainer and plot it on the deformed MeshesContainer
disp_op = dpf.operators.result.displacement(
    data_sources=model.metadata.data_sources, mesh=meshes_cont
)
disp_fc = disp_op.outputs.fields_container()
meshes_cont.plot(
    disp_fc,
    deform_by=disp_result,
    scale_factor=scale_factor,
    title="MeshesContainer",
    text="MeshesContainer.plot(disp_fc)",
)
