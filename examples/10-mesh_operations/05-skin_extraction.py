"""
.. _ref_skin_mesh:

Extract the skin from a mesh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Extracting the skin of a mesh to reduce the amount of data to operate on
can be useful for specific results and for performance.

.. note::
    This example requires the Premium ServerContext.
    For more information, see :ref:`_ref_getting_started_contexts`.

"""
# Import necessary modules
from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops


dpf.set_default_server_context(dpf.AvailableServerContexts.premium)

###############################################################################
# Create a model object to establish a connection with an
# example result file and then extract:
model = dpf.Model(examples.download_multi_stage_cyclic_result())
print(model)

###############################################################################
# Create the workflow
# ~~~~~~~~~~~~~~~~~~~~
# Maximum principal stress usually occurs on the skin of the
# model. Computing results only on this skin reduces the data size.

# Create a simple workflow computing the principal stress on the skin
# of the model.

skin_op = ops.mesh.external_layer(model.metadata.meshed_region)
skin_mesh = skin_op.outputs.mesh()

###############################################################################
# Plot the mesh skin:
skin_mesh.plot()

###############################################################################
# Compute the stress on skin nodes only:
stress = model.results.stress.on_mesh_scoping(
    skin_op.outputs.nodes_mesh_scoping).eval()

###############################################################################
# Plot the stress field on the skin mesh:
skin_mesh.plot(stress)
