from ansys.dpf import core as dpf
import time

dpf.set_default_server_context(dpf.AvailableServerContexts.premium)

########################
"""If we want to connect a remote machine"""
# server = dpf.start_local_server()
########################

dpf.load_library(r'Ans.Dpf.CFF.dll', "cff")


#################----------------- Test Code Time performance and Mesh Quality #################-----------------

def TestBigFile(path, inputs, key, my_Zone_Scoping):
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

    ds_mesh_provider = dpf.DataSources()
    ds_mesh_provider.set_result_file_path(path, key)

    ########################
    """-------
    Initialize the inputs
    -------"""
    ########################

    for input_index, input_value in enumerate(inputs):
        if input_value == 3:
            op_stream_provider = dpf.operators.metadata.streams_provider(data_sources=ds_mesh_provider)
            print("Specification for input ", input_value, "is ", op_mesh_provider.specification.inputs[input_value])
            op_mesh_provider.connect(input_value, op_stream_provider)
        elif input_value == 4:
            print("Specification for input ", input_value, "is ", op_mesh_provider.specification.inputs[input_value])
            op_mesh_provider.connect(input_value, ds_mesh_provider)
        elif input_value == 7:
            print("Specification for input ", input_value, "is ", op_mesh_provider.specification.inputs[input_value])
            op_mesh_provider.connect(input_value, my_Zone_Scoping)

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
