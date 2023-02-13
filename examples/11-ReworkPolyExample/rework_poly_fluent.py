#
# First import the required modules
from ansys.dpf import core as dpf
from ansys.dpf.core import mesh_scoping_factory

#
# # Set the premium server and the cff library
dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
server = dpf.start_local_server()

# ##############################################################################
"""NODE COORDINATE"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define the coordinates of the nodes of the polyhedron
polyhedron_points = [
    [0.01, -0.01, 0.],                                  # Node 0
    [-0.01, -0.01, 0.],                                 # Node 1
    [1.00000000e-02, 8.67361738e-19, 0.00000000e+00],   # Node 2
    [-1.00000000e-02, 2.34804084e-18, 0.00000000e+00],  # Node 3
    [8.67361738e-19, 1.00000000e-02, 0.00000000e+00],   # Node 4
    [-0.01, -0.01, 0.02],                               # Node 5
    [0.01, -0.01, 0.02],                                # Node 6
    [1.00000000e-02, 8.67361738e-19, 2.00000000e-02],   # Node 7
    [8.67361738e-19, 1.00000000e-02, 2.00000000e-02],   # Node 8
    [-1.00000000e-02, 2.34804084e-18, 2.00000000e-02],  # Node 9
]


###############################################################################
# Create a bare mesh with pre-reserved memory
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

mesh_SolidOnly = dpf.MeshedRegion(num_nodes=len(polyhedron_points), num_elements=1)

mesh_ShellOnly = dpf.MeshedRegion(num_nodes=len(polyhedron_points), num_elements=1)

# Add the nodes to the MeshedRegion
"""ShellOnly"""
for i, node in enumerate(mesh_ShellOnly.nodes.add_nodes(num=len(polyhedron_points))):
    node.id = i + 1
    node.coordinates = polyhedron_points[i]

##########################################

"""SolidOnly"""
for i, node in enumerate(mesh_SolidOnly.nodes.add_nodes(num=len(polyhedron_points))):
    node.id = i + 1
    node.coordinates = polyhedron_points[i]


###############################################################################
"""FACE_NODE connectivity"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""ShellOnly"""
polygon_faces_node_connectivity = [
    [0, 1],     # Line[Node] 0
    [0, 2],     # Line[Node] 1
    [0, 6],     # Line[Node] 2
    [1, 3],     # Line[Node] 3
    [1, 5],     # Line[Node] 4
    [2, 3],     # Line[Node] 5
    [2, 4],     # Line[Node] 6
    [2, 7],     # Line[Node] 7
    [3, 4],     # Line[Node] 8
    [3, 9],     # Line[Node] 9
    [4, 8],     # Line[Node] 10
    [5, 6],     # Line[Node] 11
    [5, 9],     # Line[Node] 12
    [6, 7],     # Line[Node] 13
    [7, 8],     # Line[Node] 14
    [7, 9],     # Line[Node] 15
    [8, 9],     # Line[Node] 16
]

"""SolidOnly"""
polyhedron_faces_node_connectivity = [
    [2, 7, 9, 3],               # Face[Node] 0
    [0, 2, 3, 1],               # Face[Node] 1
    [2, 4, 3],                  # Face[Node] 2
    [0, 1, 5, 6],               # Face[Node] 3
    [0, 6, 7, 2],               # Face[Node] 4
    [1, 3, 9, 5],               # Face[Node] 5
    [2, 7, 8, 4],               # Face[Node] 6
    [7, 9, 8],                  # Face[Node] 7
    [4, 8, 9, 3],               # Face[Node] 8
    [6, 5, 9, 7],               # Face[Node] 9
]


##########################################
"""CELL_NODE"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""ShellOnly"""
polygon_element_node_connectivity = [
    [2, 7, 9, 3],               # Face[Node] 0
    [0, 2, 3, 1],               # Face[Node] 1
    [2, 4, 3],                  # Face[Node] 2
    [0, 1, 5, 6],               # Face[Node] 3
    [0, 6, 7, 2],               # Face[Node] 4
    [1, 3, 9, 5],               # Face[Node] 5
    [2, 7, 8, 4],               # Face[Node] 6
    [7, 9, 8],                  # Face[Node] 7
    [4, 8, 9, 3],               # Face[Node] 8
    [6, 5, 9, 7],               # Face[Node] 9
]


"""SolidOnly"""
polyhedron_element_node_connectivity = [
    [2, 7, 9, 3, 0, 6, 5, 1],   # Volume[Node] 0
    [2, 4, 3, 7, 8, 9],         # Volume[Node] 1
]


##########################################
"""CELL_FACE connectivity"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""ShellOnly"""
polygon_element_faces_connectivity = [
    [7, 15, 9, 5],          # Face[Line] 0
    [1, 5, 3, 0],           # Face[Line] 1
    [6, 8, 3],              # Face[Line] 2
    [0, 4, 11, 2],          # Face[Line] 3
    [2, 13, 7, 1],          # Face[Line] 4
    [3, 9, 12, 4],          # Face[Line] 5
    [7, 14, 10, 6],         # Face[Line] 6
    [15, 16, 14],           # Face[Line] 7
    [10, 16, 9, 8],         # Face[Line] 8
    [11, 12, 15, 13],       # Face[Line] 9
]

"""SolidOnly"""
polyhedron_element_faces_connectivity = [
    [0, 1, 3, 4, 5, 9],
    [2, 6, 7, 8, 0],
]

###############################################################################
# Set the ELEMENT_FACE reverse scoping
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""ShellOnly"""
data_reverse_scoping_shell = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 1, 1],
]

"""SolidOnly"""
data_reverse_scoping_solid = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
]


###############################################################################
# Set the connectivity into a PropertyField
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""ShellOnly"""
# Set the ``"faces_nodes_connectivity"``
connectivity_f_n_shell = dpf.PropertyField()
for face_nodes_index_shell, face_nodes_shell in enumerate(polygon_faces_node_connectivity):
    connectivity_f_n_shell.append(face_nodes_shell, face_nodes_index_shell)
mesh_ShellOnly.set_property_field(property_name="faces_nodes_connectivity", value=connectivity_f_n_shell)

# Set the ``"elements_faces_connectivity"``
# Set the ``"reverse_elements_faces_connectivity"``
connectivity_e_f_shell = dpf.PropertyField()
reverse_connectivity_e_f_shell = dpf.PropertyField()
for element_faces_index_shell, element_faces_shell in enumerate(polygon_element_faces_connectivity):
    connectivity_e_f_shell.append(element_faces_shell, element_faces_index_shell)
    reverse_connectivity_e_f_shell.append(data_reverse_scoping_shell, element_faces_index_shell)

mesh_ShellOnly.set_property_field(property_name="elements_faces_connectivity", value=connectivity_e_f_shell)
mesh_ShellOnly.set_property_field(property_name="reverse_elements_faces_connectivity",
                                  value=reverse_connectivity_e_f_shell)

# Set the ``"elements_nodes_connectivity"``
connectivity_e_n_shell = dpf.PropertyField()
for element_nodes_index_shell, element_nodes_shell in enumerate(polygon_element_node_connectivity):
    connectivity_e_n_shell.append(element_nodes_shell, element_nodes_index_shell)
mesh_ShellOnly.set_property_field(property_name="elements_nodes_connectivity", value=connectivity_e_n_shell)

##########################################

"""SolidOnly"""
# Set the ``"faces_nodes_connectivity"``
connectivity_f_n_solid = dpf.PropertyField()
for face_nodes_index_solid, face_nodes_solid in enumerate(polyhedron_faces_node_connectivity):
    connectivity_f_n_solid.append(face_nodes_solid, face_nodes_index_solid)
mesh_SolidOnly.set_property_field(property_name="faces_nodes_connectivity", value=connectivity_f_n_solid)

# Set the ``"elements_faces_connectivity"``
# Set the ``"reverse_elements_faces_connectivity"`
connectivity_e_f_solid = dpf.PropertyField()
reverse_connectivity_e_f_solid = dpf.PropertyField()
for element_faces_index_solid, element_faces_solid in enumerate(polygon_element_faces_connectivity):
    connectivity_e_f_solid.append(element_faces_solid, element_faces_index_solid)
    reverse_connectivity_e_f_solid.append(data_reverse_scoping_solid, element_faces_index_solid)

mesh_SolidOnly.set_property_field(property_name="elements_faces_connectivity", value=connectivity_e_f_solid)
mesh_SolidOnly.set_property_field(property_name="reverse_elements_faces_connectivity",
                                  value=reverse_connectivity_e_f_solid)

# Set the ``"elements_nodes_connectivity"``
connectivity_e_n_solid = dpf.PropertyField()
for element_nodes_index_solid, element_nodes_solid in enumerate(polyhedron_element_node_connectivity):
    connectivity_e_n_solid.append(element_nodes_solid, element_nodes_index_solid)
mesh_SolidOnly.set_property_field(property_name="elements_nodes_connectivity", value=connectivity_e_n_solid)

###############################################################################
# Set the element/face type into a propertyfield

"""ShellOnly"""
# face types
FT_Shell = [[dpf.element_types.Line2.value]]
fcs_types_shell = dpf.PropertyField()
for face_index_solid, fctype in enumerate(FT_Shell):
    fcs_types_shell.append(fctype, face_index_solid)
fcs_types_shell.scoping = mesh_scoping_factory.elemental_scoping([1])
mesh_ShellOnly.set_property_field(property_name="fctype", value=fcs_types_shell)

# cell types
ET_Shell_Tri = [[dpf.element_types.Tri3.value]]
ET_Shell_Quad = [[dpf.element_types.Quad4.value]]
ET_Shell_Tot = ET_Shell_Tri + ET_Shell_Quad
els_types_shell = dpf.PropertyField()
for element_index_solid, eltype in enumerate(ET_Shell_Tot):
    els_types_shell.append(eltype, element_index_solid)
els_types_shell.scoping = mesh_scoping_factory.elemental_scoping([1])
mesh_ShellOnly.set_property_field(property_name="eltype", value=els_types_shell)

##########################################

"""SolidOnly"""
# face types
FT_Solid_Quad = [[dpf.element_types.Quad4.value]]
FT_Solid_PolyG = [[dpf.element_types.Polygon.value]]
FT_tot = FT_Solid_PolyG + FT_Solid_Quad

fcs_types_solid = dpf.PropertyField()
for face_index_shell, fctype in enumerate(FT_tot):
    fcs_types_solid.append(fctype, face_index_shell)
fcs_types_solid.scoping = mesh_scoping_factory.elemental_scoping([1])
mesh_SolidOnly.set_property_field(property_name="fctype", value=fcs_types_solid)

# cell types
ET_Solid = [[dpf.element_types.Polyhedron.value]]
els_types_solid = dpf.PropertyField()
for element_index_shell, eltype in enumerate(ET_Solid):
    els_types_solid.append(eltype, element_index_shell)
els_types_solid.scoping = mesh_scoping_factory.elemental_scoping([1])
mesh_SolidOnly.set_property_field(property_name="eltype", value=els_types_solid)

###############################################################################
