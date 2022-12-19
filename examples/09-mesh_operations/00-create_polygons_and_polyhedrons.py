# noqa: D400
"""
.. _create_polygons_and_polyhedrons:

Create and display a mesh with polygon and polyhedron elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to manually create a
:class:`MeshedRegion <ansys.dpf.meshed_region.MeshedRegion>`
object with two elements, a polygon and a polyhedron.

"""

# First import the required modules
from ansys.dpf import core as dpf

###############################################################################
# Define the node coordinates
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define the coordinates of the nodes of the polygon
polygon_points = [
    [0.02, 0.0, 0.0],
    [0.02, 0.01, 0.0],
    [0.03, 0.01, 0.0],
    [0.035, 0.005, 0.0],
    [0.03, 0.0, 0.0],
]

# Define the coordinates of the nodes of the polyhedron
polyhedron_points = [
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

coordinates = polygon_points + polyhedron_points

###############################################################################
# Create a bare mesh with pre-reserved memory
mesh = dpf.MeshedRegion(num_nodes=len(coordinates), num_elements=2)

# Add the nodes to the MeshedRegion
for i, node in enumerate(mesh.nodes.add_nodes(num=len(coordinates))):
    node.id = i + 1
    node.coordinates = coordinates[i]

###############################################################################
# Define the polygon's connectivity using node indices (not IDs)
connectivity = [0, 1, 2, 3, 4]

polygon_faces_connectivity = [connectivity]

# Add the polygon element to the MeshedRegion
mesh.elements.add_shell_element(id=1, connectivity=connectivity)

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
mesh.elements.add_solid_element(id=2, connectivity=connectivity)

###############################################################################
# Set property fields required for Polyhedron elements

# Set the ``"faces_nodes_connectivity"``
# :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`
faces_connectivity = polygon_faces_connectivity + polyhedron_faces_connectivity
connectivity_f = dpf.PropertyField()
for face_index, face_connectivity in enumerate(faces_connectivity):
    connectivity_f.append(face_connectivity, face_index)
mesh.set_property_field(property_name="faces_nodes_connectivity", value=connectivity_f)

# Set the ``"elements_faces_connectivity"``
# :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`
polygon_faces = [[0]]
polyhedron_faces = [[1, 2, 3, 4, 5, 6, 7]]
element_faces = polygon_faces + polyhedron_faces
elements_faces_f = dpf.PropertyField()
for element_index, element_faces in enumerate(element_faces):
    elements_faces_f.append(element_faces, element_index)
mesh.set_property_field(property_name="elements_faces_connectivity", value=elements_faces_f)

###############################################################################
# Visualize mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Plot the :class:`MeshedRegion <ansys.dpf.meshed_region.MeshedRegion>`
mesh.plot()
