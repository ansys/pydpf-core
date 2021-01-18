"""
.. _ref_basic_cyclic:

Modal Cyclic symmetry Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to to expand cyclic mesh and results

"""
import numpy as np

from ansys.dpf import core as dpf
from ansys.dpf.core import examples

###############################################################################
# Next, create the model and display the state of the result.  

model = dpf.Model(examples.simple_cyclic)
print(model)


###############################################################################
# Expand displacement results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In this example we expand displacement results, by default on all nodes 
# and the first time step

# Create displacement cyclic operator   
UCyc = model.operator("mapdl::rst::U_cyclic")

#expand the displacements and get a total deformation
nrm = dpf.Operator("norm_fc")
nrm.inputs.connect(UCyc.outputs)
fields = nrm.outputs.fields_container()

# get the expanded mesh
mesh = UCyc.outputs.expanded_meshed_region.get_data()

#plot the expanded result on the expanded mesh
mesh.plot(fields[0])

###############################################################################
#
# Expand stresses at a given time step
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#define stress expansion operator and request stresses at time set = 8
SCyc = model.operator("mapdl::rst::S_cyclic")
SCyc.inputs.time_scoping.connect([8])

#request the results averaged on the nodes
SCyc.inputs.requested_location.connect("Nodal")

#connect the base mesh and the expanded mesh, to avoid rexpanding the mesh
SCyc.inputs.sector_mesh.connect(model.metadata.meshed_region)
SCyc.inputs.expanded_meshed_region.connect(mesh)

#request equivalent von mises operator and connect it to stress operator
eqv = dpf.Operator("eqv_fc")
eqv.inputs.connect(SCyc.outputs)

#expand the results and get stress eqv
fields = eqv.outputs.fields_container()


#plot the expanded result on the expanded mesh
mesh.plot(fields[0])


###############################################################################
#
# Expand stresses at given sectors
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#define stress expansion operator and request stresses at time set = 8
SCyc = model.operator("mapdl::rst::S_cyclic")
SCyc.inputs.time_scoping.connect([8])

#request the results averaged on the nodes
SCyc.inputs.requested_location.connect("Nodal")

#connect the base mesh and the expanded mesh, to avoid rexpanding the mesh
SCyc.inputs.sector_mesh.connect(model.metadata.meshed_region)
SCyc.inputs.expanded_meshed_region.connect(mesh)

#request results on sectors 1, 3 and 5
SCyc.inputs.sectors_to_expand.connect([1,3,5])

#extract Sy (use component selector and select the component 1)
comp_sel = dpf.Operator("component_selector_fc")
comp_sel.inputs.fields_container.connect(SCyc.outputs.fields_container)
comp_sel.inputs.component_number.connect(0)

#expand the displacements and get the resuls
fields = comp_sel.outputs.fields_container()

#plot the expanded result on the expanded mesh
mesh.plot(fields[0])
