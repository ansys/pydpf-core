#
# First import the required modules
from ansys.dpf import core as dpf
from ansys.dpf.core import mesh_scoping_factory
import numpy
#
# # Set the premium server and the cff library
dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
server = dpf.start_local_server()

dpf.set_default_server_context(dpf.AvailableServerContexts.premium)

# ##############################################################################
"""NODE COORDINATE"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define the coordinates of the nodes of the polyhedron
polyhedron_points = [
    [0, 0, 0],  # 0
    [0, 0, 0],  # 1
    [0, 0, 0],  # 2
    [0, 0, 0],  # 3
    [0, 0, 0],  # 4
    [0, 0, 0],  # 5
    [0, 0, 0],  # 6
    [0, 0, 0],  # 7
    [0, 0, 0],  # 8
    [0, 0, 0],  # 9
    [9.99999978e-03, 8.74136522e-20, 0.00000000e+00],       # 10
    [0.00000000e+00, -3.30139302e-19, 9.99999978e-03],       # 11
    [0.00525, 0.005, 0.00525],                              # 12
    [9.99999978e-03, -3.14418395e-20, 9.99999978e-03],  # 13
    [0.00000000e+00, 1.03134572e-19, -9.99999978e-03],  # 14
    [0.00525, 0.005, -0.00475],  # 15
    [9.99999978e-03, 2.06269144e-19, -9.99999978e-03],  # 16
    [-9.99999978e-03, -3.14418382e-19, 0.00000000e+00],  # 17
    [-0.00475, 0.005, -0.00475],  # 18
    [-9.99999978e-03, 4.50853098e-34, -9.99999978e-03],  # 19
    [-0.00475, 0.005, 0.00525],  # 20
    [-9.99999978e-03, -6.28836764e-19, 9.99999978e-03],  # 21
    [0.0005, 0.01, 0.0005],  # 22
    [-7.24078460e-03, 2.62782397e-03, 8.26236179e-20],  # 23
    [-7.10436800e-20, 2.37844935e-03, 7.74047290e-03],  # 24
    [8.67361738e-19, 2.62782397e-03, -7.24078460e-03],  # 25
    [0.00774047, 0.00237845, 0],  # 26
    [-9.39159748e-36, -1.57209197e-20, 1.73472348e-18],  # 28
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
    [15, 17],       # Line[Node] 0
    [17, 18],       # Line[Node] 1
    [18, 13],       # Line[Node] 2
    [13, 8],        # Line[Node] 3
    [8, 15],        # Line[Node] 4
    [13, 7],        # Line[Node] 5
    [7, 17],        # Line[Node] 6
    [18, 14],       # Line[Node] 7
    [14, 1],        # Line[Node] 8
    [16, 17],       # Line[Node] 9
    [14, 2],        # Line[Node] 10
    [2, 16],        # Line[Node] 11
    [16, 0],        # Line[Node] 12
    [0, 17],        # Line[Node] 13
    [17, 15],       # Line[Node] 14
    [15, 4],        # Line[Node] 15
    [4, 17],        # Line[Node] 16
    [15, 5],        # Line[Node] 17
    [5, 16],        # Line[Node] 18
    [13, 10],       # Line[Node] 19
    [10, 14],       # Line[Node] 20
    [0, 3],         # Line[Node] 21
    [3, 2],         # Line[Node] 22
    [3, 1],         # Line[Node] 23
    [11, 1],        # Line[Node] 24
    [1, 17],        # Line[Node] 25
    [7, 11],        # Line[Node] 26
    [6, 0],         # Line[Node] 27
    [16, 5],        # Line[Node] 28
    [5, 6],         # Line[Node] 29
    [4, 6],         # Line[Node] 30
    [9, 4],         # Line[Node] 31
    [8, 9],         # Line[Node] 32
    [8, 13],        # Line[Node] 33
    [7, 9],         # Line[Node] 34
    [14, 1],        # Line[Node] 35
    [11, 10],       # Line[Node] 36
    [12, 2],        # Line[Node] 37
    [10, 12],       # Line[Node] 38
    [5, 12],        # Line[Node] 39
    [8, 12]         # Line[Node] 40
]

"""SolidOnly"""
polyhedron_faces_node_connectivity = [
    [15, 17, 18, 13, 8],        # Face[Node] 0
    [17, 18, 13, 7],            # Face[Node] 1
    [17, 18, 14, 1],            # Face[Node] 2
    [16, 17, 18, 14, 2],        # Face[Node] 3
    [17, 16, 0],                # Face[Node] 4
    [17, 15, 4],                # Face[Node] 5
    [16, 17, 15, 5],            # Face[Node] 6
    [14, 18, 13, 10],           # Face[Node] 7
    [2, 16, 0, 3],              # Face[Node] 8
    [3, 1, 14, 2],              # Face[Node] 9
    [11, 1, 17, 7],             # Face[Node] 10
    [6, 0, 16, 5],              # Face[Node] 11
    [5, 15, 4, 6],              # Face[Node] 12
    [3, 0, 17, 1],              # Face[Node] 13
    [9, 4, 15, 8],              # Face[Node] 14
    [8, 13, 7, 9],              # Face[Node] 15
    [7, 17, 4, 9],              # Face[Node] 16
    [10, 14, 1, 11],            # Face[Node] 17
    [11, 7, 13, 10],            # Face[Node] 18
    [4, 17, 0, 6],              # Face[Node] 19
    [12, 2, 14, 10],            # Face[Node] 20
    [10, 13, 8, 12],            # Face[Node] 21
    [8, 15, 5, 12],             # Face[Node] 22
    [5, 16, 2, 12],             # Face[Node] 23
]


##########################################
"""CELL_NODE"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""ShellOnly"""
polygon_element_node_connectivity = [
    [15, 17, 18, 13, 8],        # Face[Node] 0
    [17, 18, 13, 7],            # Face[Node] 1
    [17, 18, 14, 1],            # Face[Node] 2
    [16, 17, 18, 14, 2],        # Face[Node] 3
    [17, 16, 0],                # Face[Node] 4
    [17, 15, 4],                # Face[Node] 5
    [16, 17, 15, 5],            # Face[Node] 6
    [14, 18, 13, 10],           # Face[Node] 7
    [2, 16, 0, 3],              # Face[Node] 8
    [3, 1, 14, 2],              # Face[Node] 9
    [11, 1, 17, 7],             # Face[Node] 10
    [6, 0, 16, 5],              # Face[Node] 11
    [5, 15, 4, 6],              # Face[Node] 12
    [3, 0, 17, 1],              # Face[Node] 13
    [9, 4, 15, 8],              # Face[Node] 14
    [8, 13, 7, 9],              # Face[Node] 15
    [7, 17, 4, 9],              # Face[Node] 16
    [10, 14, 1, 11],            # Face[Node] 17
    [11, 7, 13, 10],            # Face[Node] 18
    [4, 17, 0, 6],              # Face[Node] 19
    [12, 2, 14, 10],            # Face[Node] 20
    [10, 13, 8, 12],            # Face[Node] 21
    [8, 15, 5, 12],             # Face[Node] 22
    [5, 16, 2, 12],             # Face[Node] 23
]


"""SolidOnly"""
polyhedron_element_node_connectivity = [
    [2, 5, 8, 10, 12, 13, 14, 15, 16, 17, 18],  # Volume[Node] 0
    [0, 1, 2, 3, 14, 16, 17, 18],               # Volume[Node] 1
    [4, 7, 8, 9, 13, 15, 17, 18],               # Volume[Node] 2
    [0, 4, 5, 6, 15, 16, 17],                   # Volume[Node] 3
    [1, 7, 10, 11, 13, 14, 17, 18],             # Volume[Node] 4
]


##########################################
"""CELL_FACE connectivity"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""ShellOnly"""
polygon_element_faces_connectivity = [
    [0, 1, 2, 3, 4],            # Face[Line] 0
    [1, 2, 5, 6],               # Face[Line] 1
    [1, 7, 8, 9],               # Face[Line] 2
    [9, 1, 7, 10],              # Face[Line] 3
    [9, 12, 13],                # Face[Line] 4
    [14, 15, 16],               # Face[Line] 5
    [9, 14, 17, 18],            # Face[Line] 6
    [7, 2, 19, 20],             # Face[Line] 7
    [11, 12, 21, 22],           # Face[Line] 8
    [23, 8, 10, 12],            # Face[Line] 9
    [24, 25, 6, 26],            # Face[Line] 10
    [27, 12, 18, 29],           # Face[Line] 11
    [17, 15, 30, 29],           # Face[Line] 12
    [21, 13, 25, 23],           # Face[Line] 13
    [31, 15, 4, 32],            # Face[Line] 14
    [33, 5, 34, 32],            # Face[Line] 15
    [6, 16, 31, 34],            # Face[Line] 16
    [20, 35, 24, 36],           # Face[Line] 17
    [26, 5, 19, 36],            # Face[Line] 18
    [16, 13, 27, 30],           # Face[Line] 19
    [37, 10, 20, 38],           # Face[Line] 20
    [19, 33, 40, 38],           # Face[Line] 21
    [4, 17, 39, 40],            # Face[Line] 22
    [18, 11, 37, 39],           # Face[Line] 23
]

"""SolidOnly"""
polyhedron_element_faces_connectivity = [
    [3, 7, 20, 21, 22, 23, 0, 6],   # Volume[Face] 0
    [2, 8, 9, 13, 3, 4],            # Volume[Face] 1
    [0, 5, 14, 15, 16],             # Volume[Face] 2
    [4, 6, 11, 12, 19, 5],          # Volume[Face] 3
    [1, 10, 17, 18, 2, 7],          # Volume[Face] 4
]

###############################################################################
# Set the ELEMENT_FACE reverse scoping
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""ShellOnly"""
data_reverse_scoping_shell = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 1, 1],
]

"""SolidOnly"""
data_reverse_scoping_solid = [
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1],
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
    reverse_connectivity_e_f_shell.append(data_reverse_scoping_shell[element_faces_index_shell], element_faces_index_shell)

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
for element_faces_index_solid, element_faces_solid in enumerate(polyhedron_element_faces_connectivity):
    connectivity_e_f_solid.append(element_faces_solid, element_faces_index_solid)
    reverse_connectivity_e_f_solid.append(data_reverse_scoping_solid[element_faces_index_solid], element_faces_index_solid)

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
ET_Shell_Poly = [[dpf.element_types.Polygon.value]]

ET_Shell_Tot = ET_Shell_Tri + ET_Shell_Quad + ET_Shell_Poly

els_types_shell = dpf.PropertyField()
for element_index_solid, eltype in enumerate(ET_Shell_Tot):
    els_types_shell.append(eltype, element_index_solid)
els_types_shell.scoping = mesh_scoping_factory.elemental_scoping([1])
mesh_ShellOnly.set_property_field(property_name="eltype", value=els_types_shell)

##########################################

"""SolidOnly"""
# face types
FT_Solid_Tri = [[dpf.element_types.Tri3.value]]
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
