# noqa: D400
"""
.. _polyhedron_custom_mesh:

Create and display mesh with polygon and polyhedron elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to manually create a
:class:`MeshedRegion <ansys.dpf.meshed_region.MeshedRegion>`
object with two elements, a polygon and a polyhedron.

First, import the required modules
"""

from ansys.dpf import core as dpf

###############################################################################
# Create the polyhedron element
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define the points of the polyhedron
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

###############################################################################
# Define the faces and elements connectivity
faces_connectivity = [
    [0, 1, 2, 3, 4],
    [0, 1, 6, 5],
    [0, 4, 9, 5],
    [4, 9, 8, 3],
    [3, 8, 7, 2],
    [2, 7, 6, 1],
    [5, 6, 7, 8, 9],
]
elements_faces = [[0, 1, 2, 3, 4, 5, 6]]

###############################################################################
# Build the element connectivity from faces connectivity
element_connectivity = [i for face in faces_connectivity for i in face]

###############################################################################
# Create mesh object and add nodes and elements
mesh = dpf.MeshedRegion()
for index, node_coordinates in enumerate(polyhedron_points):
    mesh.nodes.add_node(index, node_coordinates)
mesh.elements.add_solid_element(0, element_connectivity)

###############################################################################
# Set the ``"faces_nodes_connectivity"``
# :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`
connectivity_f = dpf.PropertyField()
for face_index, face_connectivity in enumerate(faces_connectivity):
    connectivity_f.append(face_connectivity, face_index)
mesh.set_property_field("faces_nodes_connectivity", connectivity_f)

###############################################################################
# Set the ``"elements_faces_connectivity"``
# :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`
elements_faces_f = dpf.PropertyField()
for element_index, element_faces in enumerate(elements_faces):
    elements_faces_f.append(element_faces, element_index)
mesh.set_property_field("elements_faces_connectivity", elements_faces_f)

###############################################################################
# Create the polygon element
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create and add a polygon element to the same mesh object. Define the points of the polygon
polygon_points = [
    [0.02, 0.0, 0.0],
    [0.02, 0.01, 0.0],
    [0.03, 0.01, 0.0],
    [0.035, 0.005, 0.0],
    [0.03, 0.0, 0.0],
]

###############################################################################
# Define the polygon's connectivity
connectivity = [10, 11, 12, 13, 14]

###############################################################################
# Add polygon's nodes and element to the mesh object
for id, node in enumerate(polygon_points):
    mesh.nodes.add_node(id, node)
mesh.elements.add_shell_element(0, connectivity)

###############################################################################
# Visualize mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Plot the :class:`MeshedRegion <ansys.dpf.meshed_region.MeshedRegion>`
mesh.plot()
