"""

DPF-Core Fatigue Engineering Simple Example
~~~~~~~~~~~~~~~~~~~~
This example shows how to generate and use a result file to calculate the 
cycles to failure result for a simple model.

Material data is manually imported, Structural Steel from Ansys Mechanical:
Youngs Modulus (youngsSteel)
Poisson's Ratio (prxySteel)
Cycles to Failure (snData)

The first step is to generate a simple model with high stress and save the 
results .rst locally to myDir (default C:\temp).
For this we use a short pyMapdl script

The second step uses DPF-Core to generate the cycles to failure result.
The locally saved rst is imported and plotted.
Then the von Mises stress is generated and plotted with DPF operators.
The python package numpy is then used to interpolate the cycles to failure values.
The nodal von Mises equivalent stress value is used in the interpolation.
Note the cycles to failure data needs to be manipulated to use numpy interpolation.

An empty field is created and filled with the resulting cycles to failure values.
Cycles to failure result plotted.

The cycles to failure result is the (interpolated) negative of the stress result.
The higher the stress result, the lower the number of cycles to failure.

Start MAPDL as a service to generate the rst file
and import the DPF-Core module as ``dpf_core``.
"""


from ansys.mapdl.core import launch_mapdl
from ansys.dpf import core as dpf
import numpy as np
myDir = r'c:\temp'

## Material parameters from Ansys Mechanical - Structural Steel
youngsSteel = 200e9
prxySteel = 0.3
snData = np.empty((11, 2)) # initialize empty np matrix
snData[:, 0] = [10, 20, 50, 100, 200, 2000, 10000, 20000, 1e5, 2e5, 1e6]
snData[:, 1] = [3.999e9, 2.8327e9, 1.896e9, 1.413e9, 1.069e9, 4.41e8, 2.62e8, 2.14e8, 1.38e8, 1.14e8, 8.62e7]

#### Launch pymapdl to generate rst file in myDir
mapdl = launch_mapdl()
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
model = dpf.Model(os.path.join(mapdl.directory, 'file.rst'))
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
myResult[:, 1] = vm_stress
myResult[:, 2] = np.interp(myResult[:, 1], xPoints, yValues)

###############################################################################

# Create an empty field, add nodes/results and plot
myResultField = dpf.Field(len(myNodes), dpf.natures.scalar, 'Nodal')
my_scoping = dpf.Scoping()
my_scoping.location = 'Nodal'
my_scoping.ids = myResult[:, 0]
myResultField.scoping = my_scoping
myResultField.data =  myResult[:, 2]
mesh.plot(myResultField)
