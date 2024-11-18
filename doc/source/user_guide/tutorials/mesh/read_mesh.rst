.. _tutorials_read_mesh:

====================================
Read the mesh definition information
====================================

.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |DataSources| replace:: :class:`Model <ansys.dpf.core.data_sources.DataSources>`
.. |MeshInfo| replace:: :class:`MeshInfo <ansys.dpf.core.mesh_info.MeshInfo>`
.. |Nodes| replace:: :class:`Nodes <ansys.dpf.core.nodes.Nodes>`
.. |Elements| replace:: :class:`Elements <ansys.dpf.core.elements.Elements>`
.. |Faces| replace:: :class:`Faces <ansys.dpf.core.faces.Faces>`
.. |Scoping| replace:: :class:`Scoping <ansys.dpf.core.scoping.Scoping>`
.. |PropertyField| replace:: :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`

This tutorial explains how to access and read a mesh.

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your
own by scratch or by getting it from a result file. For more information check the
:ref:`tutorials_create_a_mesh_from_scratch` and :ref:`tutorials_get_mesh_from_result_file` tutorials.

There is a general method to read the |MeshedRegion| by manipulating
the methods of this object (see :ref: `read_mesh_general` ).

Nevertheless, if you have a mesh from a LSDYNA, Fluent or CFX file we have a
special object to read more specific metadata information by
exploring the |MeshInfo| object (see :ref: `read_mesh_fluids_lsdyna`).

.. _read_mesh_general:

Read a |MeshedRegion|
---------------------

Define the mesh
^^^^^^^^^^^^^^^

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your
own by scratch or by getting it from a result file. For more information check the
:ref:`tutorials_create_a_mesh_from_scratch` and :ref:`tutorials_get_mesh_from_result_file` tutorials.

Here we we will download a  result file available in our `Examples` package.
For more information about how to import your result file in DPF check
the :ref:`ref_tutorials_import_data` tutorial section.

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    # Define the result file
    result_file_path_1 = examples.find_static_rst()
    # Create the model
    my_model_1 = dpf.Model(data_sources=result_file_path_1)
    # Get the mesh
    my_meshed_region_1 = my_model_1.metadata.meshed_region

Read the mesh
^^^^^^^^^^^^^

From the |MeshedRegion| you can access its information by manipulating this object properties.
The mesh information includes :

- Unit;
- Nodes, elements and faces;
- Named selections;
- Properties.

Check all the information you can get at: |MeshedRegion|.

When instantiating the nodes, element, faces and named selection you get the correspondent DPF objects:
|Nodes|,|Elements|,|Faces| and |Scoping|. For example:

.. code-block:: python

    # Get the mesh elements
    my_nodes = my_meshed_region_1.nodes
    # Print the nodes
    print(my_nodes)
    print(type(my_nodes))

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    result_file_path_1 = examples.find_static_rst()
    my_model_1 = dpf.Model(data_sources=result_file_path_1)
    my_meshed_region_1 = my_model_1.metadata.meshed_region
    my_nodes = my_meshed_region_1.nodes
    print(my_nodes)
    print(type(my_nodes))

When handling properties you can check which are the available ones and then
chose those you want to extract.

.. code-block:: python

    # Get the available properties
    my_available_props = my_meshed_region_1.available_property_fields
    # Print the available properties
    print(my_available_props)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_available_props = my_meshed_region_1.available_property_fields
    print(my_available_props)

When extracting those properties you get a |PropertyField| with that information. Their data is mapped
to the entity their are defined at:

.. code-block:: python

    # Get the element types on the mesh
    my_el_types = my_meshed_region_1.property_field(property_name="eltype")
    # Print the element types
    print(my_el_types)


.. _read_mesh_fluids_lsdyna:

Read the mesh of a LSDYNA, Fluent or CFX file
---------------------------------------------

Define the mesh
^^^^^^^^^^^^^^^

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your
own by scratch or by getting it from a result file. For more information check the
:ref:`tutorials_create_a_mesh_from_scratch` and :ref:`tutorials_get_mesh_from_result_file` tutorials.

Here we we will download a  result file available in our `Examples` package.
For more information about how to import your result file in DPF check
the :ref:`ref_tutorials_import_data` tutorial section.

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    # Define the result file
    result_file_path_2 = examples.download_fluent_axial_comp()["flprj"]
    # Create the model
    my_model_2 = dpf.Model(data_sources=result_file_path_2)
    # Get the mesh
    my_meshed_region_2 = my_model.metadata.meshed_region

Read the mesh
^^^^^^^^^^^^^

The |Model| is a helper designed to give shortcuts to access the analysis results
metadata, by opening a DataSources or a Streams, and to instanciate results provider
for it.

From the |Model| you can access the |MeshedRegion| metadata information. The mesh metadata information
includes :

- Properties;
- Parts;
- Faces;
- Bodies;
- Zones;
- Number of nodes and elements;
- Elements types.

Get the the mesh metadata information and print the available ones:

.. code-block:: python

    # Get the mesh metadata information
    my_mesh_info = my_model_2.metadata.mesh_info
    # Print the mesh metadata information
    print(my_mesh_info)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    result_file_path_2 = examples.download_fluent_axial_comp()["flprj"]
    my_model_2 = dpf.Model(data_sources=result_file_path_2)
    my_meshed_region_2 = my_model_2.metadata.meshed_region
    my_mesh_info = my_model_2.metadata.mesh_info
    print(my_mesh_info)

You can access each of those mesh information's by manipulating the |MeshInfo| object properties.
For example we can check the cell zone names:

.. code-block:: python

    # Get the cell zone names
    my_cell_zones = my_mesh_info.get_property("cell_zone_names")
    print(my_cell_zones)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_cell_zones = my_mesh_info.get_property("cell_zone_names")
    print(my_cell_zones)

For more information on reading a mesh from a LSDYNA, Fluent or CFX file check the examples sections:
:ref:`fluids_examples` and :ref:`examples_cfx`
