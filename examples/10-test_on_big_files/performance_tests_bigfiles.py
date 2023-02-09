from ansys.dpf import core as dpf
import time
from ansys.dpf.core import examples

dpf.set_default_server_context(dpf.AvailableServerContexts.premium)
server = dpf.start_local_server()

dpf.load_library(r'C:\Program Files\ANSYS Inc\v232\dpf\bin\winx64\Ans.Dpf.CFF.dll', "cff")

ds_mesh_provider = dpf.DataSources()
# ds_mesh_provider.set_result_file_path(
#     r"C:\Users\mnale\OneDrive - ANSYS, Inc\Desktop\big_files_perf_tests\CFF_big\VOF\Mesh\hull-component.cas.h5", "cas")
#
ds_mesh_provider.set_result_file_path(
    r"D:\Dependencies\builddeps\cff\Ans.Dpf.CFF\Ans.Dpf.CFFTest\test_models\FLPRJ\axial_comp\axial_comp_reduced.flprj")


#################----------------- Test Code Time performance and Mesh Quality #################-----------------

######------ Instanciate the mesh_provider operators ######------

op_mesh_provider = dpf.operators.mesh.mesh_provider()


###--- Definition of the input pin for the mesh_provider operator ###---
"""Big files only need data sources or stream container"""


##-- Data Source Input Pin = 4 ##--
"""result file path container, used if no streams are set"""

op_mesh_provider.inputs.data_sources.connect(ds_mesh_provider)


##-- Stream container Input Pin = 3 ##--
"""result file container allowed to be kept open to cache data"""

op_stream_provider = dpf.operators.metadata.streams_provider(data_sources=ds_mesh_provider)

op_mesh_provider.inputs.streams_container.connect(op_stream_provider)


###--- Definition of the output pin for the mesh_provider operator ###---

start_time_mesh = time.time()
mesh_p = op_mesh_provider.outputs.mesh()
elapsed_time_mesh = time.time() - start_time_mesh

print("\n", "#####################################################################")
print("Time performance for meshing process: ", elapsed_time_mesh, "sec")
print("#####################################################################", "\n")

print(op_mesh_provider.eval(0), "\n")




######------ Working from MeshedRegion ######------

print("##########################################################################################################################################")
print("First we work using a meshed region from a Model define by our data source")
print("##########################################################################################################################################","\n")


###--- Extract info from MeshedRegion ###---

model = dpf.Model(data_sources=ds_mesh_provider)
meshed_region = model.metadata.meshed_region

##-- Element ##--

element_meshed_region = meshed_region.elements
print("Number of elements: ", element_meshed_region.n_elements,"\n")

elements_scoping_meshed_region = element_meshed_region.scoping

print("#####################################################################")
print(elements_scoping_meshed_region)
print("#####################################################################","\n")

##-- Nodes ##--

nodes_meshed_region = meshed_region.nodes
print("Number of nodes:", nodes_meshed_region.n_nodes)

nodes_scoping_meshed_region = nodes_meshed_region.scoping
nodes_coordinate_field_meshed_region = nodes_meshed_region.coordinates_field

print("#####################################################################")
print(nodes_scoping_meshed_region)
print("#####################################################################","\n")
print(nodes_coordinate_field_meshed_region)


######------ Working on workflows from mesh_provider operator ######------

print("##########################################################################################################################################")
print("Then we use mesh_provider operator")
print("##########################################################################################################################################","\n")

###--- Element ids scoping from mesh ###---
"""Get the elements ids scoping of a given input mesh."""
op_elements_from_mesh = dpf.operators.scoping.elemental_from_mesh(mesh=mesh_p)

op_elements_from_mesh.inputs.mesh.connect(mesh_p)

start_time_element_mesh_scoping = time.time()
element_mesh_scoping = op_elements_from_mesh.outputs.mesh_scoping()
elapsed_time_element_mesh_scoping = time.time() - start_time_element_mesh_scoping

print("#####################################################################")
print("Time performance for mesh element ids scoping process: ", elapsed_time_element_mesh_scoping, "sec")
print("#####################################################################", "\n")

print(op_elements_from_mesh.eval(0))


###--- Nodes ids scoping from mesh ###---
"""Get the nodes ids scoping of an input mesh."""
op_nodes_from_mesh = dpf.operators.scoping.nodal_from_mesh(mesh=mesh_p)

op_nodes_from_mesh.inputs.mesh.connect(mesh_p)

start_time_node_mesh_scoping = time.time()
nodes_scoping = op_nodes_from_mesh.outputs.mesh_scoping()
elapsed_time_node_mesh_scoping = time.time() - start_time_node_mesh_scoping

print("#####################################################################")
print("Time performance for node ids scoping process: ", elapsed_time_node_mesh_scoping, "sec")
print("#####################################################################", "\n")

print(op_nodes_from_mesh.eval(0))


###--- Nodes coordinates from mesh ###---
"""Returns the node coordinates of the mesh(es) in input"""
op_node_coordinates = dpf.operators.mesh.node_coordinates()

op_node_coordinates.inputs.mesh.connect(mesh_p)

start_time_node_coordinate = time.time()
field_of_coordinates = op_node_coordinates.outputs.coordinates_as_field()
elapsed_time_node_coordinate = time.time() - start_time_node_coordinate

print("#####################################################################")
print("Time performance for node coordinate process: ", elapsed_time_node_coordinate, "sec")
print("#####################################################################", "\n")

print(op_node_coordinates.eval())


###--- Elemental Scoping on coordinates ###---
"""Finds the Elemental scoping of a set of coordinates. """
op_scoping_on_coordinate = dpf.operators.mapping.scoping_on_coordinates()

op_scoping_on_coordinate.inputs.coordinates.connect(nodes_coordinate_field_meshed_region)
op_scoping_on_coordinate.inputs.mesh.connect(mesh_p)

start_time_field_coordinate = time.time()
element_scoping = op_scoping_on_coordinate.outputs.scoping()
elapsed_time_field_coordinate = time.time() - start_time_field_coordinate

print("#####################################################################")
print("Time performance for field of coordinate process: ", elapsed_time_field_coordinate, "sec")
print("#####################################################################", "\n")

print(op_scoping_on_coordinate.eval())


###--- Node ids from elements scoping ###---
"""Returns the ordered node ids corresponding to the element ids scoping in input.
For each element the node ids are its connectivity."""
op_connectivity_from_element = dpf.operators.scoping.connectivity_ids()

my_take_mid_nodes = True

op_connectivity_from_element.inputs.mesh_scoping.connect(elements_scoping_meshed_region)
op_connectivity_from_element.inputs.mesh.connect(mesh_p)
op_connectivity_from_element.inputs.take_mid_nodes.connect(my_take_mid_nodes)

start_time_connectivity_elemental = time.time()
connectivity_elemental_scoping = op_connectivity_from_element.outputs.elemental_scoping()
elapsed_time_connectivity_elemental = time.time() - start_time_connectivity_elemental

start_time_connectivity_mesh_scoping = time.time()
connectivity_mesh_scoping = op_connectivity_from_element.outputs.mesh_scoping()
elapsed_time_connectivity_mesh_scoping = time.time() - start_time_connectivity_mesh_scoping

print("#####################################################################")
print("Time performance for elemental connectivity process: ", elapsed_time_connectivity_elemental, "sec")
print("#####################################################################")
print("Time performance for mesh scoping connectivity process: ", elapsed_time_connectivity_mesh_scoping, "sec")
print("#####################################################################", "\n")

print(op_connectivity_from_element.eval(0))
print(op_connectivity_from_element.eval(1))

print("#####################################################################", "\n")


###--- Plot the mesh ###---
mesh_p.plot()
