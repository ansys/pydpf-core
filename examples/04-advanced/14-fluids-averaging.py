"""
.. _ref_fluids_averaging:

Nodal reconstruction for Elemental and Face results
------------------------------------------------------

This example demonstrates how you can postprocess Fluent results. In particular,
it demonstrates the specific averaging capabilities to reconstruct to the nodes
results defined on centroids of Elements and Faces.
"""

###############################################################################
# Import the result file and create a model

import ansys.dpf.core as dpf
from ansys.dpf.core import examples

path = examples.download_fluent_axial_comp()["flprj"]
ds = dpf.DataSources(path)
model = dpf.Model(data_sources=ds)

###############################################################################
# Explore the available results through the ResultInfo. This is a Fluent model
# whose native results are exported to either the centroid of the elements (like
# Enthalpy or RMS Temperature), the centroid of the faces (like the Mass Flow Rate)
# or the centroid of both elements and faces (like Static Pressure).

print(model.metadata.result_info)

###############################################################################
# Explore the mesh through the MeshInfo. The MeshInfo provides metadata information
# about the mesh. For fluid models, it is useful to know the cell and face zones,
# as well as the topological relationships between them. First get all the available
# information in the MeshInfo

minfo = model.metadata.mesh_info
print(
    "\n".join(
        "{}\t{}".format(k, v)
        for k, v in minfo.generic_data_container.get_property_description().items()
    )
)

###############################################################################
# Then, get the bodies and their names in the model. In this model there are two
# bodies

print(minfo.get_property("body_name"))

###############################################################################
# Each body is comprised of a set of cell zones. You can investigate the hierarchical
# relationship between bodies and cell zones. In this case, each body is only comprised
# of one cell zone

print(minfo.get_property("body_cell_topology"))

###############################################################################
# Similarly, each body is limited by a set of face zones (generally representing
# boundary conditions of the model). You can investigate the hierarchical
# relationship between bodies and face zones. In this case, each body is limited
# by several face zones

print(minfo.get_property("body_face_topology"))

###############################################################################
# The body and face zone ids shown in the previous PropertyFields can be mapped
# to their names

print(minfo.get_property("cell_zone_names"))
# print(minfo.get_property("face_zone_names")) # hangs forever. infinite loop¿
