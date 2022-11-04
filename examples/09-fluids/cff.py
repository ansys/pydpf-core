import os
from ansys.dpf import core as dpf

from ansys.dpf.core.dpf_operator import available_operator_names


# WARNING: For this script to work as intended one needs the CFF plugin installed

# Verify the CFF operators have been correctly loaded from the plugin on the server side.
server = dpf.start_local_server()
available_operators = available_operator_names(server=server)
cff_operators = [operator for operator in available_operators if "cff::" in operator]
print(cff_operators)

# Define where the Polys.cas.h5 file can be found locally.
data_path = r"D:\ANSYSDev\Sandbox\cff\Ans.Dpf.CFF\Ans.Dpf.CFFTest\test_models\fluent\3D"
cas_path = os.path.join(data_path, r"Polys\Polys.cas.h5")
dat_path = cas_path

# Create the DataSources.
ds = dpf.DataSources()
ds.set_result_file_path(cas_path, "cas")
ds.add_file_path(dat_path, "dat")
print(ds)

# Create a Model based on this DataSources.
model = dpf.Model(data_sources=ds)
print(model)

# Try and plot the mesh.
model.plot(opacity=0.3)


# Create a mesh with only the first element for easier debugging.
# DOES NOT WORK -> Problem with the face_nodes_connectivity property field for that case.
# mesh = model.metadata.meshed_region
# scoping = dpf.mesh_scoping_factory.elemental_scoping([mesh.elements.scoping.ids[0]])
# mesh2 = dpf.operators.mesh.from_scoping(scoping=scoping,
#                                         mesh=mesh).eval()
# print(mesh2)
# mesh2.plot()
# print(dir(model.results))
