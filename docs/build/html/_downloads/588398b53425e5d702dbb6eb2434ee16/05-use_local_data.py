"""
.. _ref_use_local_data_example:

Bring Field's data locally to improve performances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Using the as_local_field option allows to bring the server's
data locally and to work only on the local process before sending the data
updates to the server on one shot at the end.
Reducing the number of calls to the server is key to improve
performances.
"""
import numpy as np

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops

###############################################################################
# First, create a model object to establish a connection with an
# example result file and then extract
model = dpf.Model(examples.download_multi_stage_cyclic_result())
print(model)



###############################################################################
# Create the Workflow
# ~~~~~~~~~~~~~~~~~~~~
# Create a simple workflow computing the principal stress on the skin
# of the model. Principal stress maximul usually occurs on the skin of the 
# model, computing results only on this skin allows to reduce data sizes

skin_op = ops.mesh.external_layer(model.metadata.meshed_region)
skin_mesh = skin_op.outputs.mesh()

###############################################################################
# Plot the mesh skin
skin_mesh.plot()


###############################################################################
# Compute the stress principal inveriants on the skin nodes only
stress_op = ops.result.stress(data_sources=model.metadata.data_sources)
stress_op.inputs.requested_location.connect(dpf.locations.nodal)
stress_op.inputs.mesh_scoping.connect(skin_op.outputs.nodes_mesh_scoping)


principal_op = ops.invariant.principal_invariants_fc(stress_op)
principal_stress_1 = principal_op.outputs.fields_eig_1()[0]
principal_stress_2 = principal_op.outputs.fields_eig_2()[0]
principal_stress_3 = principal_op.outputs.fields_eig_3()[0]



###############################################################################
# Manipulate data locally
# ~~~~~~~~~~~~~~~~~~~~~~~


###############################################################################
# As an example, we will go over the fields, keep the largest invariant value
# by node if the averaged value of invariants is large enough
# Exploring data allows the user add his own custom needs easily

node_scoping_ids = principal_stress_1.scoping.ids
threshold = 300000.

field_to_keep = dpf.fields_factory.create_scalar_field(len(node_scoping_ids), location=dpf.locations.nodal)

with field_to_keep.as_local_field() as f:
    with principal_stress_1.as_local_field() as s1:
        with principal_stress_2.as_local_field() as s2:
            with principal_stress_3.as_local_field() as s3:
                for i,id in enumerate(node_scoping_ids):
                    d1 = abs(s1.get_entity_data_by_id(id))
                    d2 = abs(s2.get_entity_data_by_id(id))
                    d3 = abs(s3.get_entity_data_by_id(id))
                    if (d1+d2+d3)/3. > threshold :
                        d = max(d1,d2,d3)
                        f.append(d, id)


###############################################################################
# Plot the result field
# ~~~~~~~~~~~~~~~~~~~~~~~


###############################################################################
# Plot the result field on the skin mesh
skin_mesh.plot(field_to_keep)


###############################################################################
# Plot the initial invariants
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

skin_mesh.plot(principal_stress_1)
skin_mesh.plot(principal_stress_2)
skin_mesh.plot(principal_stress_3)
                    
                    

