# -*- coding: utf-8 -*-

"""
The first step is to generate a simple model with high stress and save the results .rst locally
For this we use a short pyMapdl code
"""

from ansys.mapdl.core import launch_mapdl
from ansys.dpf import core as dpf
import numpy as np
myDir = r'c:\temp'

## Material parameters from Ansys Mechanical Structural Steel
youngsSteel = 200e9
prxySteel = 0.3
snData = np.empty((11, 2)) # initialize empty np matrix
snData[:, 0] = [10, 20, 50, 100, 200, 2000, 10000, 20000, 1e5, 2e5, 1e6]
snData[:, 1] = [3.999e9, 2.8327e9, 1.896e9, 1.413e9, 1.069e9, 4.41e8, 2.62e8, 2.14e8, 1.38e8, 1.14e8, 8.62e7]

#### Launch pymapdl to generate rst file in myDir
mapdl = launch_mapdl(run_location=myDir)
mapdl.prep7()
# Model
mapdl.cylind(0.5, 0, 10, 0)
mapdl.mp("EX", 1, youngsSteel)
mapdl.mp("PRXY", 1, prxySteel)
mapdl.mshape(key = 1, dimension = '3d')
mapdl.et(1, "SOLID186")
mapdl.esize(0.3)
mapdl.vmesh('ALL')

# #### Boundary Conditions: fixed constraint
mapdl.nsel(type_='S', item='LOC', comp ='Z', vmin = 0)
mapdl.d("all", "all")
mapdl.nsel(type_='S', item='LOC', comp ='Z', vmin = 10)
nnodes = mapdl.get("NumNodes" , "NODE", 0, "COUNT" )
mapdl.f(node = "ALL", lab = "fy", value =  -13e6/nnodes)
mapdl.allsel()

# #### Solve
mapdl.run("/SOLU")
sol_output = mapdl.solve()
mapdl.exit()
print('apdl model solved.')

# ##### pydpf is used to post process the .rst in order to estimate the cycles to failure
model = dpf.Model(myDir + '\\file.rst')
print(model)
mesh = model.metadata.meshed_region

# Get the von mises equivalent stress, requires an operator
s_eqv_op = dpf.operators.result.stress_von_mises()
s_eqv_op.inputs.data_sources.connect(model)
vm_stress_fields = s_eqv_op.outputs.fields_container()
vm_stress_nodal = vm_stress_fields[0]
vm_stress_nodal.plot()

# Use numpy to interpolate the results.
vm_stress = vm_stress_nodal.data
myNodes = vm_stress_nodal.scoping.ids
xPoints = snData[:, 1][::-1] # the x values are the stress ranges in ascending order
yValues = snData[:, 0][::-1] # y values are inverted cycles to failure

myResult = np.ones((len(myNodes), 3))
myResult[:, 0] = myNodes
myResult[:, 1] = vm_stress # UNITS!!!!
myResult[:, 2] = np.interp(myResult[:, 1], xPoints, yValues)

##Create an empty field, add nodes/results and plot
myResultField = dpf.Field(len(myNodes), dpf.natures.scalar, 'Nodal')
my_scoping = dpf.Scoping()
my_scoping.location = 'Nodal'
my_scoping.ids = myResult[:, 0]
myResultField.scoping = my_scoping
myResultField.data =  myResult[:, 2]
mesh.plot(myResultField)
# This is a way to plot w/out units/label

""" The cycles to failure result is the (interpolated) negative of the stress result.
The higher the stress result, the lower number of cycles to failure. """
