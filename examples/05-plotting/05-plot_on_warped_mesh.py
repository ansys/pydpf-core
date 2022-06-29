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
model = dpf.Model(examples.multishells_rst)
print(model)
model.plot(title='Model', text='Model.plot()')

# Define a scaling factor and a step for the field to be used for warping.
scaling_factor = 0.001
step = 1

# Define the result to warp by
disp_result = model.results.displacement.on_time_scoping([step])

# Get the mesh and plot it as a deformed geometry
mesh = model.metadata.meshed_region
mesh.plot(warp_by=disp_result, scaling_factor=scaling_factor,
          title='MeshedRegion', text='MeshedRegion.plot()')

# Get the displacement field
disp_fc = disp_result.eval()
disp_field = disp_fc[0]

# Plot it on the deformed geometry directly
disp_field.plot(warp_by=disp_result, scaling_factor=scaling_factor,
                title='Field', text='Field.plot()')
# or by applying it to the mesh
mesh.plot(disp_field, warp_by=disp_result, scaling_factor=scaling_factor,
          title='MeshedRegion', text='MeshedRegion.plot(disp_field)')

# Split the model by material and plot the deformed MeshesContainer obtained
split_mesh_op = dpf.Operator("split_mesh")
split_mesh_op.connect(7, mesh)
split_mesh_op.connect(13, "mat")
meshes_cont = split_mesh_op.get_output(0, dpf.types.meshes_container)
meshes_cont.plot(warp_by=disp_result, scaling_factor=scaling_factor,
                 title='MeshesContainer', text='MeshesContainer.plot()')

# Create a corresponding FieldsContainer and plot it on the deformed MeshesContainer
disp_op = dpf.Operator("U")
disp_op.connect(7, meshes_cont)
ds = dpf.DataSources(examples.multishells_rst)
disp_op.connect(4, ds)
disp_fc = disp_op.outputs.fields_container()
meshes_cont.plot(disp_fc, warp_by=disp_result, scaling_factor=scaling_factor,
                 title='MeshesContainer', text='MeshesContainer.plot(disp_fc)')
