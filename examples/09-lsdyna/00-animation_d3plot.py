import os
from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

res_path = r"D:\AFT\DPF\PyDyna\projectile-erosion_files\dp0\SYS\MECH"
ds = dpf.DataSources()
d3plot_path = os.path.join(res_path, "d3plot")
ds.set_result_file_path(d3plot_path, 'd3plot')

time_scoping = dpf.Scoping(ids=range(1, 23))

mesh_op = dpf.Operator("lsdyna::d3plot::meshes_provider")
mesh_op.inputs.data_sources.connect(ds)
mesh_op.inputs.time_scoping.connect(time_scoping)
meshes = mesh_op.outputs.meshes()

disp = dpf.Operator("lsdyna::d3plot::U")
disp.inputs.data_sources.connect(ds)
disp.inputs.time_scoping.connect(time_scoping)
fields = disp.outputs.displacement()

for index in range(1, 23):
    fields[index - 1].meshed_region = meshes.get_mesh({'time': index})

fields.animate(save_as="test.gif")