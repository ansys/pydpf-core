# noqa: D400
"""
.. _create_polygons_and_polyhedrons:

Create and display a mesh with polygon and polyhedron elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to manually create a
:class:`MeshedRegion <ansys.dpf.meshed_region.MeshedRegion>`
object with two elements, a polygon and a polyhedron.

"""
#
# First import the required modules
from ansys.dpf import core as dpf
from ansys.dpf.core import mesh_scoping_factory
#
# # Set the premium server and the cff library
dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
server = dpf.start_local_server()

###############################################################################
# Define the node coordinates
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define the coordinates of the nodes of the polygon
polygon_points = [
    [0.02, 0.0, 0.0],  # 0
    [0.02, 0.01, 0.0],  # 1
    [0.03, 0.01, 0.0],  # 2
    [0.035, 0.005, 0.0],  # 3
    [0.03, 0.0, 0.0],  # 4
]

# Define the coordinates of the nodes of the polyhedron
polyhedron_points = [
    [0.02, 0.0, 0.02],  # 5
    [0.02, 0.01, 0.02],  # 6
    [0.03, 0.01, 0.02],  # 7
    [0.035, 0.005, 0.02],  # 8
    [0.03, 0.0, 0.02],  # 9
    [0.02, 0.0, 0.03],  # 10
    [0.02, 0.01, 0.03],  # 11
    [0.03, 0.01, 0.03],  # 12
    [0.035, 0.005, 0.03],  # 13
    [0.03, 0.0, 0.03],  # 14
]

coordinates_ShellOnly = polygon_points
coordinates_SolidOnly = polygon_points + polyhedron_points

###############################################################################
# Create a bare mesh with pre-reserved memory

mesh_ShellOnly = dpf.MeshedRegion(num_nodes=len(coordinates_ShellOnly), num_elements=1)
mesh_SolidOnly = dpf.MeshedRegion(num_nodes=len(coordinates_SolidOnly), num_elements=1)

# Add the nodes to the MeshedRegion
######## On ajoute les nodes à la mesh ########
for i, node in enumerate(mesh_ShellOnly.nodes.add_nodes(num=len(coordinates_ShellOnly))):
    node.id = i + 1
    node.coordinates = coordinates_ShellOnly[i]

for i, node in enumerate(mesh_SolidOnly.nodes.add_nodes(num=len(coordinates_SolidOnly))):
    node.id = i + 1
    node.coordinates = coordinates_SolidOnly[i]

###############################################################################
# Define the polygon's connectivity using node indices (not IDs)
######## On a une premiere connectivity pour le polygone i.e. on lie les nodes entre eux pour faire une face ########

connectivity = [0, 1, 2, 3, 4]
polygon_faces_connectivity = [connectivity]

# Add the polygon element to the MeshedRegion

mesh_ShellOnly.elements.add_shell_element(id=1, connectivity=connectivity)

###############################################################################
# Define the polyhedron's connectivity

# Define the faces connectivity
polyhedron_faces_connectivity = [
    [5, 6, 7, 8, 9],
    [5, 6, 11, 10],
    [5, 9, 14, 10],
    [9, 14, 13, 8],
    [8, 13, 12, 7],
    [7, 12, 11, 6],
    [10, 11, 12, 13, 14],
]

# Build the polyhedron's nodal connectivity from faces connectivity
connectivity = [i for face in polyhedron_faces_connectivity for i in face]

# Add the polyhedron element to the MeshedRegion
mesh_SolidOnly.elements.add_solid_element(id=2, connectivity=connectivity)

###############################################################################
# Set property fields required for Polyhedron elements

# Set the ``"faces_nodes_connectivity"``
# :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`
faces_connectivity = polygon_faces_connectivity + polyhedron_faces_connectivity
connectivity_f = dpf.PropertyField()
for face_index, face_connectivity in enumerate(faces_connectivity):
    connectivity_f.append(face_connectivity, face_index)
mesh_ShellOnly.set_property_field(property_name="faces_nodes_connectivity", value=connectivity_f)

# Set the ``"elements_faces_connectivity"``
# :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`
polygon_faces = [[0]]
polyhedron_faces = [[1, 2, 3, 4, 5, 6, 7]]
element_faces = polygon_faces + polyhedron_faces
elements_faces_f = dpf.PropertyField()
for element_index, element_faces in enumerate(element_faces):
    elements_faces_f.append(element_faces, element_index)
mesh_SolidOnly.set_property_field(property_name="elements_faces_connectivity", value=elements_faces_f)

# Set the ``"elements_faces_reversed_connectivity"``
# :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`
polygon_faces = [[0]]
polyhedron_faces = [[1, 2, 3, 4, 5, 6, 7]]
for i in range(len(polyhedron_faces)):
    polyhedron_faces_reverse = list(reversed(polyhedron_faces[i]))
element_faces_reverse = polygon_faces + polyhedron_faces
elements_faces_reverse_f = dpf.PropertyField()
for element_index, element_faces in enumerate(element_faces):
    elements_faces_reverse_f.append(element_faces, element_index)
mesh_SolidOnly.set_property_field(property_name="elements_faces_reversed", value=elements_faces_reverse_f)

# Set the ``"cell_types"``
# :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`
ET = [[dpf.element_types.Polyhedron.value]]
els_types = dpf.PropertyField()
for element_index, el_type in enumerate(ET):
    els_types.append(el_type, element_index)
els_types.scoping = mesh_scoping_factory.elemental_scoping([2])
mesh_SolidOnly.set_property_field(property_name="eltype", value=els_types)

###############################################################################
# Visualize mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Plot the :class:`MeshedRegion <ansys.dpf.meshed_region.MeshedRegion>`
mesh_ShellOnly.plot()

mesh_SolidOnly.plot()

#Il faut:
"""~~~~~~~~ Spliter les face-nodes pour les polygons
   ~~~~~~~~ Les elements-faces pour les polyhedrons
   ~~~~~~~~ Faire attention aux scoping
   ~~~~~~~~ Definir les cells type pour le polyhedron
   ~~~~~~~~ Faire la doc
   ~~~~~~~~ Voir comment faire pour les cells-nodes connectivity"""