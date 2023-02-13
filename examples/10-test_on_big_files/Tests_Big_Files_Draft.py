import matplotlib.pyplot as plt

from ansys.dpf import core as dpf
import time
import sys
import numpy

numpy.set_printoptions(threshold=sys.maxsize)

dpf.set_default_server_context(dpf.AvailableServerContexts.premium)

# ########################
# """If we want to connect a remote machine"""
# # server = dpf.start_local_server()
# ########################
#
# dpf.load_library(r'Ans.Dpf.CFF.dll', "cff")
#
# #################----------------- Test Code Time performance and Mesh Quality #################-----------------
#
# #############------------- mesh_provider operator #############-------------
#
# ########################
# """-------
# Instanciate the mesh_provider operators
# -------"""
# ########################
#
# op_meshes_provider = dpf.Operator(r"cff::cas::meshes_provider")
#
# ########################
# """-------
# Define the data source
# -------"""
# ########################
#
# path = "D:/Dependencies/builddeps/cff/Ans.Dpf.CFF/Ans.Dpf.CFFTest/test_models/fluent/3D/Polys/Polys.cas.h5"
# key = "cas"
#
# ds_mesh_provider = dpf.DataSources()
# ds_mesh_provider.set_result_file_path(path, key)
#
# my_Zone_Scoping = 0
#
# ########################
# """-------
# Initialize the inputs
# -------"""
# ########################
#
# op_stream_provider = dpf.operators.metadata.streams_provider(data_sources=ds_mesh_provider)
# print("Specification for input ", 3, "is ", op_meshes_provider.specification.inputs[3])
# op_meshes_provider.connect(3, op_stream_provider)
#
# ########################
# """-------
# Definition of the output pin for the mesh_provider operator
# -------"""
# ########################
#
# mesh_p = op_meshes_provider.eval(0)
# mesh0 = mesh_p[0]
# meshout = mesh_p[1]
#
# print("mesh 0:", "\n",
#       mesh0, "\n")
# print("mesh 1:", "\n",
#       meshout)
#
# elements_faces_connectivity_field = meshout.property_field("elements_faces_connectivity")
# elements_nodes_connectivity_field = meshout.elements.connectivities_field
# faces_nodes_connectivity_field = meshout.property_field("faces_nodes_connectivity")
# nodes_connectivity_field = meshout.nodes.nodal_connectivity_field
#
# number_of_nodes = meshout.nodes.n_nodes
# number_of_elements = meshout.elements.n_elements
#
# for i in range(0, number_of_elements):
#     print(elements_faces_connectivity_field.get_entity_data(i))
#
# print("##################################")
#
# for i in range(0, number_of_elements):
#     print(elements_nodes_connectivity_field.get_entity_data(i))
#
# print("##################################")
#
# for i in range(0, 24):
#     print(faces_nodes_connectivity_field.get_entity_data(i))
#
# print("##################################")
#
# for i in range(0, number_of_nodes):
#     print(nodes_connectivity_field.get_entity_data(i))
#

########################################################################################################################################################################################################################

########################
"""If we want to connect a remote machine"""
# server = dpf.start_local_server()
########################

dpf.load_library(r'Ans.Dpf.CFF.dll', "cff")

#################----------------- Test Code Time performance and Mesh Quality #################-----------------

#############------------- mesh_provider operator #############-------------

########################
"""-------
Instanciate the mesh_provider operators
-------"""
########################

op_mesh_provider = dpf.Operator(r"cff::cas::mesh_provider")

########################
"""-------
Define the data source
-------"""
########################

# path = "C:/Users/mnale/OneDrive - ANSYS, Inc/Desktop/big_files_perf_tests/CFF_big/airline_all/airline.cas.h5"
path = "D:/Dependencies/builddeps/cff/Ans.Dpf.CFF/Ans.Dpf.CFFTest/test_models/fluent/3D/Polys/Polys.cas.h5"
key = "cas"
input_optionnal_value = 7

ds_mesh_provider = dpf.DataSources()
ds_mesh_provider.set_result_file_path(path, key)

my_Zone_Scoping = 0

########################
"""-------
Initialize the inputs
-------"""
########################

op_stream_provider = dpf.operators.metadata.streams_provider(data_sources=ds_mesh_provider)
print("Specification for input ", 3, "is ", op_mesh_provider.specification.inputs[3])
op_mesh_provider.connect(3, op_stream_provider)

if input_optionnal_value == 4:
    print("Specification for input ", input_optionnal_value, "is ",
          op_mesh_provider.specification.inputs[input_optionnal_value])
    op_mesh_provider.connect(input_optionnal_value, ds_mesh_provider)
elif input_optionnal_value == 7:
    print("Specification for input ", input_optionnal_value, "is ",
          op_mesh_provider.specification.inputs[input_optionnal_value])
    op_mesh_provider.connect(input_optionnal_value, """my_Zone_Scoping""")

########################
"""-------
Definition of the output pin for the mesh_provider operator
-------"""
########################

start_time_mesh = time.time()
mesh_p = op_mesh_provider.eval(0)
elapsed_time_mesh = time.time() - start_time_mesh

print("\n", "#####################################################################")
print("Time performance for meshing process: ", elapsed_time_mesh, "sec", "\n")
print(mesh_p)
print("#####################################################################", "\n")

########################
"""-------
Evaluation of the mesh to get info
-------"""
########################


#############------------- quality of the mesh using mesh_p #############-------------

###--- Element ids scoping from mesh ###---

########################
"""Get the elements ids scoping of a given input mesh."""
########################

start_time_element_mesh_scoping = time.time()
element_mesh_scoping = mesh_p.elements.scoping
elapsed_time_element_mesh_scoping = time.time() - start_time_element_mesh_scoping

print("#####################################################################")
print("Time performance for mesh element ids scoping process: ", elapsed_time_element_mesh_scoping, "sec", "\n")
print(element_mesh_scoping)
print("#####################################################################", "\n")

###--- Nodes ids scoping from mesh ###---

########################
"""Get the nodes ids scoping of an input mesh."""
########################

start_time_node_mesh_scoping = time.time()
nodes_scoping = mesh_p.nodes.scoping
elapsed_time_node_mesh_scoping = time.time() - start_time_node_mesh_scoping

print("#####################################################################")
print("Time performance for node ids scoping process: ", elapsed_time_node_mesh_scoping, "sec", "\n")
print(nodes_scoping)
print("#####################################################################", "\n")

###--- Nodes coordinates from mesh ###---

########################
"""Returns the node coordinates of the mesh(es) in input"""
########################

start_time_node_coordinate = time.time()
field_of_coordinates = mesh_p.nodes.coordinates_field
elapsed_time_node_coordinate = time.time() - start_time_node_coordinate

print("#####################################################################")
print("Time performance for node coordinate process: ", elapsed_time_node_coordinate, "sec", "\n")
print(field_of_coordinates)
print("#####################################################################", "\n")

###--- Node ids from elements scoping ###---

########################
"""Returns the ordered node ids corresponding to the element ids scoping in input.
For each element the node ids are its connectivity."""
########################

""" For fluids it's not relevant """
my_take_mid_nodes = True

start_time_connectivity_elemental = time.time()
connectivity_elemental_scoping = mesh_p.elements.connectivities_field
elapsed_time_connectivity_elemental = time.time() - start_time_connectivity_elemental

print("#####################################################################")
print("Time performance for elemental connectivity process: ", elapsed_time_connectivity_elemental, "sec", "\n")
print(connectivity_elemental_scoping)
print("#####################################################################", "\n")

mesh_p.plot()

