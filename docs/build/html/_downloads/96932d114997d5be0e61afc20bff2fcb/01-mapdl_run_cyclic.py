"""
.. _ref_mapdl_run_cyclic:

Use Mapdl run and get cyclic results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to make an Mapdl solve and 
how to get the cyclic expanded results. 

"""

###############################################################################
# Import dpf module 

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops
from ansys.dpf.core.help import norm, min_max
import matplotlib.pyplot as plt

import os

###############################################################################
# Run Mapdl
# =========
# Call mapdl::run operator 

mapld_run = dpf.Operator("mapdl::run")

###############################################################################
# Get dataSources and connect it to the mapdl::run operator

data_sources = dpf.DataSources(examples.cyclic_dat)
mapld_run.inputs.data_sources.connect(data_sources)

###############################################################################
# get the executable path and connect it to the operator

ansys_path = dpf.misc.find_ansys()
if os.name == 'nt':
    executable = os.path.join("winx64", "ansys2021R2.exe")
elif os.name == 'posix':
    executable = os.path.join("linx64", "ansys2021r2")
executable_path = os.path.join(ansys_path, "ansys", "bin", executable)
mapld_run.inputs.mapdl_exe_path(executable_path)

###############################################################################
# Run the operator to get the result file path as output

rst_data_sources = mapld_run.outputs.data_sources()

###############################################################################
# Read results
# ============
# Create a model from result data sources

model = dpf.Model(rst_data_sources)


###############################################################################
# Elemental nodal stress

s = model.operator("mapdl::rst::S_cyclic")
fcS = s.outputs.fields_container()

min_max_op = ops.min_max.min_max()
min_max_op.inputs.field.connect(fcS[0])

min = min_max_op.outputs.field_min()
max =  min_max_op.outputs.field_max()

print(min.data)
print(max.data)


###############################################################################
# Displacement

u = model.operator("mapdl::rst::U_cyclic")

timeIds = list(range(1, model.metadata.time_freq_support.n_sets+1))
timeIds

u.inputs.time_scoping(timeIds)
fcU = u.outputs.fields_container()

min_max_over_time = min_max(norm(u))

max_disp = min_max_over_time.outputs.field_max()

print(max_disp.data)

mesh_provider = model.metadata.mesh_provider
mesh_provider.inputs.read_cyclic(2)
mesh = mesh_provider.outputs.mesh()

mesh.plot(fcU[20])