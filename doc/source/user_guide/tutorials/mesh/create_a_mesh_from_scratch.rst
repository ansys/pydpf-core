.. _ref_tutorials_create_a_mesh_from_scratch:

==========================
Create a mesh from scratch
==========================

.. include:: ../../../links_and_refs.rst

This tutorial demonstrates how to build a |MeshedRegion| from the scratch.

The mesh object in DPF is a |MeshedRegion|. You can create your own |MeshedRegion| object and use it
with DPF operators. The ability to use scripting to create any DPF entity means
that you are not dependent on result files and can connect the DPF environment
with any Python tool.

In this tutorial, we create a parallel piped mesh made of linear hexa elements.

:jupyter-download-script:`Download tutorial as Python script<create_a_mesh_from_scratch>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<create_a_mesh_from_scratch>`

Import the necessary modules
----------------------------

Import the ``ansys.dpf.core`` module, including the operators module and the numpy library.

.. jupyter-execute::

    # Import the numpy library
    import numpy as np
    # Import the ``ansys.dpf.core`` module
    from ansys.dpf import core as dpf
    # Import the operators module
    from ansys.dpf.core import operators as ops

Define the mesh dimensions
--------------------------

.. jupyter-execute::

    # Define the mesh dimensions
    length = 0.1
    width = 0.05
    depth = 0.1
    num_nodes_in_length = 10
    num_nodes_in_width = 5
    num_nodes_in_depth = 10
    # Create a MeshedRegion object
    my_meshed_region = dpf.MeshedRegion()

Define the connectivity function
--------------------------------

To create a mesh you must define the nodes connectivity. This means to define
the nodes ids connected to each element.

Here, we create a function that will find this connectivity.

.. jupyter-execute::

    def search_sequence_numpy(arr, seq):
        """Find a sequence in an array and return its index."""
        indexes = np.where(np.isclose(arr, seq[0]))
        for index in np.nditer(indexes[0]):
            if index % 3 == 0:
                if np.allclose(arr[index + 1], seq[1]) and np.allclose(arr[index + 2], seq[2]):
                    return index
        return -1

Add nodes
---------

Add |Nodes| to the |MeshedRegion| object.

.. jupyter-execute::

    node_id = 1
    for i, x in enumerate(
        [float(i) * length / float(num_nodes_in_length) for i in range(0, num_nodes_in_length)]
    ):
        for j, y in enumerate(
            [float(i) * width / float(num_nodes_in_width) for i in range(0, num_nodes_in_width)]
        ):
            for k, z in enumerate(
                [float(i) * depth / float(num_nodes_in_depth) for i in range(0, num_nodes_in_depth)]
            ):
                my_meshed_region.nodes.add_node(node_id, [x, y, z])
                node_id += 1

Get the nodes coordinates field.

.. jupyter-execute::

    my_nodes_coordinates = my_meshed_region.nodes.coordinates_field

Set the mesh properties
-----------------------

Set the mesh unit.

.. jupyter-execute::

    my_meshed_region.unit = "mm"

Set the nodes coordinates.

.. jupyter-execute::

    # Get the nodes coordinates data
    my_nodes_coordinates_data = my_nodes_coordinates.data
    # As we use the connectivity function we need to get the data as a list
    my_nodes_coordinates_data_list = my_nodes_coordinates.data_as_list
    # Set the nodes scoping
    my_coordinates_scoping = my_nodes_coordinates.scoping

Add elements
------------
Add |Elements| to the |MeshedRegion| object.

.. jupyter-execute::

    element_id = 1
    for i, x in enumerate(
        [float(i) * length / float(num_nodes_in_length) for i in range(num_nodes_in_length - 1)]
    ):
        for j, y in enumerate(
            [float(i) * width / float(num_nodes_in_width) for i in range(num_nodes_in_width - 1)]
        ):
            for k, z in enumerate(
                [float(i) * depth / float(num_nodes_in_depth) for i in range(num_nodes_in_depth - 1)]
            ):
                coord1 = np.array([x, y, z])
                connectivity = []
                for xx in [x, x + length / float(num_nodes_in_length)]:
                    for yy in [y, y + width / float(num_nodes_in_width)]:
                        for zz in [z, z + depth / float(num_nodes_in_depth)]:
                            data_index = search_sequence_numpy(my_nodes_coordinates_data_list, [xx, yy, zz])
                            scoping_index = int(data_index / 3)  # 3components
                            connectivity.append(scoping_index)
                # rearrange connectivity
                tmp = connectivity[2]
                connectivity[2] = connectivity[3]
                connectivity[3] = tmp
                tmp = connectivity[6]
                connectivity[6] = connectivity[7]
                connectivity[7] = tmp
                my_meshed_region.elements.add_solid_element(element_id, connectivity)
                element_id += 1

Plot the mesh
-------------

You can check the mesh we just created with a plot. For more information on how to plot a mesh see
the :ref:`ref_tutorials_plotting_meshes` tutorial.

.. jupyter-execute::

    # Plot the mesh
    my_meshed_region.plot()