.. _tutorials_create_a_mesh_from_scratch:

==========================
Create a mesh from scratch
==========================

.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.field.Field>`
.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`

The mesh object in DPF is a |MeshedRegion|. You can create your own |MeshedRegion| object to use DPF operators
with your own data. The ability to use scripting to create any DPF entity means
that you are not dependent on result files and can connect the DPF environment
with any Python tool.

This tutorial demonstrates how to build a |MeshedRegion| from the scratch.

Here we create a parallel piped mesh made of linear hexa elements.

Import the necessary modules
----------------------------

Import the ``ansys.dpf.core`` module, including the operators subpackage and the numpy library

.. code-block:: python

    import numpy as np
    from ansys.dpf import core as dpf
    from ansys.dpf.core import operators as ops

Define the mesh dimensions
--------------------------

.. code-block:: python

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

To create a mesh we need to define the nodes connectivity. This means to define
the elements and nodes indices connected to each node.

Here we create a function that will find the connectivity of our entities.

.. code-block:: python

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

Add nodes to the |MeshedRegion| object:

.. code-block:: python

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

Get the nodes coordinates field

.. code-block:: python

    my_nodes_coordinates = my_meshed_region.nodes.coordinates_field

Set the mesh node properties
----------------------------

Set the mesh unit:

.. code-block:: python

    my_meshed_region.unit = "mm"

Set the nodes coordinates:

.. code-block:: python

    # Get the nodes coordinates data
    my_nodes_coordinates_data = my_nodes_coordinates.data
    # As we use the connectivity function we need to get the data as a list
    my_nodes_coordinates_data_list = my_nodes_coordinates.data_as_list
    # Get the nodes scoping
    my_coordinates_scoping = my_nodes_coordinates.scoping

Add the elements
----------------

.. code-block:: python

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

.. code-block:: python

    my_meshed_region.plot()

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    import numpy as np
    from ansys.dpf import core as dpf
    from ansys.dpf.core import operators as ops
    length = 0.1
    width = 0.05
    depth = 0.1
    num_nodes_in_length = 10
    num_nodes_in_width = 5
    num_nodes_in_depth = 10
    my_meshed_region = dpf.MeshedRegion()
    def search_sequence_numpy(arr, seq):
        """Find a sequence in an array and return its index."""
        indexes = np.where(np.isclose(arr, seq[0]))
        for index in np.nditer(indexes[0]):
            if index % 3 == 0:
                if np.allclose(arr[index + 1], seq[1]) and np.allclose(arr[index + 2], seq[2]):
                    return index
        return -1
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
    my_nodes_coordinates = my_meshed_region.nodes.coordinates_field
    my_meshed_region.unit = "mm"
    my_nodes_coordinates_data = my_nodes_coordinates.data
    my_nodes_coordinates_data_list = my_nodes_coordinates.data_as_list
    my_coordinates_scoping = my_nodes_coordinates.scoping
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
    my_meshed_region.plot()