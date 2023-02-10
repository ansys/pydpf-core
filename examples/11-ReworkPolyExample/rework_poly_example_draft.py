# First import the required modules
from ansys.dpf import core as dpf
from ansys.dpf.core import mesh_scoping_factory

#
# # Set the premium server and the cff library
dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
server = dpf.start_local_server()

# Il faut:
"""~~~~~~~~ Spliter les face-nodes pour les polygons
   ~~~~~~~~ Les elements-faces pour les polyhedrons
   ~~~~~~~~ Faire attention aux scoping
   ~~~~~~~~ Definir les cells type pour le polyhedron
   ~~~~~~~~ Faire la doc
   ~~~~~~~~ Voir comment faire pour les cells-nodes connectivity"""

coordinates = [
    [0.02, 0.0, 0.02],
    [0.02, 0.01, 0.02],
    [0.03, 0.01, 0.02],
    [0.035, 0.005, 0.02],
    [0.03, 0.0, 0.02],
    [0.02, 0.0, 0.03],
    [0.02, 0.01, 0.03],
    [0.03, 0.01, 0.03],
    [0.035, 0.005, 0.03],
    [0.03, 0.0, 0.03],
]

mesh_ShellOnly = dpf.MeshedRegion(num_nodes=len(coordinates), num_elements=1)
mesh_SolidOnly = dpf.MeshedRegion(num_nodes=len(coordinates), num_elements=2)

mesh = dpf.MeshedRegion(num_nodes=len(coordinates), num_elements=1)

for i, node in enumerate(mesh_ShellOnly.nodes.add_nodes(num=len(coordinates))):
    node.id = i+1
    node.coordinates = coordinates[i]

for i, node in enumerate(mesh_SolidOnly.nodes.add_nodes(num=len(coordinates))):
    node.id = i+1
    node.coordinates = coordinates[i]

faces_connectivity = [
    [0, 1, 2, 3, 4],
    [0, 1, 6, 5],
    [0, 4, 9, 5],
    [4, 9, 8, 3],
    [3, 8, 7, 2],
    [2, 7, 6, 1],
    [5, 6, 7, 8, 9],
]

"""Set the connectivity"""

# faces -> nodes conn
connectivity_f = dpf.PropertyField()
for face_index, face_connectivity in enumerate(faces_connectivity):
    connectivity_f.append(face_connectivity, face_index)
mesh_ShellOnly.set_property_field(property_name="faces_nodes_connectivity", value=connectivity_f)

# cells -> faces conn
element_faces = [[0, 1, 2, 3, 4, 5, 6]]
elements_faces_f = dpf.PropertyField()
for element_index, element_faces in enumerate(element_faces):
    elements_faces_f.append(element_faces, element_index)
mesh_SolidOnly.set_property_field(property_name="elements_faces_connectivity", value=elements_faces_f)

# cells -> node conn
cell_connectivity = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
connectivity_node = dpf.PropertyField()
for cell_index, cell_connectivity in enumerate(cell_connectivity):
    connectivity_node.append(cell_connectivity, cell_index)
mesh_SolidOnly.set_property_field(property_name="cell_node_connectivity", value=connectivity_node)


"""Set the type"""

# face types
FT = [[dpf.element_types.Polygon.value]]
face_types = dpf.PropertyField()
for face_index, fctype in enumerate(FT):
    face_types.append(fctype, face_index)
face_types.scoping = mesh_scoping_factory.elemental_scoping([1])
mesh_ShellOnly.set_property_field(property_name="fctype", value=face_types)

# cell types
ET = [[dpf.element_types.Polyhedron.value]]
els_types = dpf.PropertyField()
for element_index, eltype in enumerate(ET):
    els_types.append(eltype, element_index)
els_types.scoping = mesh_scoping_factory.elemental_scoping([1])
mesh_SolidOnly.set_property_field(property_name="eltype", value=els_types)

print("ShellOnly mesh:", "\n",
      mesh_ShellOnly, "\n")
print("SolidOnly mesh:", "\n",
      mesh_SolidOnly, "\n")

"""Just an example of enumerate function use"""
# values = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
#
# for count, value in enumerate(values):
#     print(count, value)
