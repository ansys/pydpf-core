.. _ref_tutorials_explore_mesh:

==============
Explore a mesh
==============

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

.. include:: ../../../links_and_refs.rst
.. |PropertyField| replace:: :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`
.. |element_types| replace:: :class:`list of available element types in a DPF mesh<ansys.dpf.core.elements.element_types>`
.. |StringField| replace:: :class:`StringField <ansys.dpf.core.string_field.StringField>`

This tutorial explains how to access a mesh data and metadata so it can be manipulated.

:jupyter-download-script:`Download tutorial as Python script<explore_mesh>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<explore_mesh>`

Define the mesh
---------------

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your
own from scratch or by getting it from a result file. For more information check the
:ref:`ref_tutorials_create_a_mesh_from_scratch` and :ref:`ref_tutorials_get_mesh_from_result_file` tutorials.

For this tutorial, we get a |MeshedRegion| from a result file. You can use one available in the |Examples| module.
For more information see the :ref:`ref_tutorials_get_mesh_from_result_file` tutorial.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module
            from ansys.dpf import core as dpf
            # Import the examples module
            from ansys.dpf.core import examples
            # Import the operators module
            from ansys.dpf.core import operators as ops

            # Define the result file path
            result_file_path_1 = examples.find_static_rst()
            # Create the model
            model_1 = dpf.Model(data_sources=result_file_path_1)
            # Get the mesh
            meshed_region_1 = model_1.metadata.meshed_region

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module
            from ansys.dpf import core as dpf
            # Import the examples module
            from ansys.dpf.core import examples
            # Import the operators module
            from ansys.dpf.core import operators as ops

            # Define the result file path
            result_file_path_2 = examples.download_d3plot_beam()
            # Create the DataSources object
            ds_2 = dpf.DataSources()
            ds_2.set_result_file_path(filepath=result_file_path_2[0], key="d3plot")
            ds_2.add_file_path(filepath=result_file_path_2[3], key="actunits")
            # Create the model
            model_2 = dpf.Model(data_sources=ds_2)
            # Get the mesh
            meshed_region_2 = model_2.metadata.meshed_region

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module
            from ansys.dpf import core as dpf
            # Import the examples module
            from ansys.dpf.core import examples
            # Import the operators module
            from ansys.dpf.core import operators as ops

            # Define the result file path
            result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]
            # Create the model
            model_3 = dpf.Model(data_sources=result_file_path_3)
            # Get the mesh
            meshed_region_3 = model_3.metadata.meshed_region

    .. tab-item:: CFX

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module
            from ansys.dpf import core as dpf
            # Import the examples module
            from ansys.dpf.core import examples
            # Import the operators module
            from ansys.dpf.core import operators as ops

            # Define the result file path
            result_file_path_4 = examples.download_cfx_mixing_elbow()
            # Create the model
            model_4 = dpf.Model(data_sources=result_file_path_4)
            # Get the mesh
            meshed_region_4 = model_4.metadata.meshed_region

Explore the mesh data
---------------------

You can access the mesh data by manipulating the |MeshedRegion| object methods.
The mesh data includes :

- Unit;
- Nodes, elements and faces;
- Named selections: .

When instantiating nodes, elements, faces and named selections you get the corresponding DPF objects:
|Nodes|, |Elements|, |Faces| and |Scoping|.

For more information of other types of data you can get from a mesh, see the API reference of the |MeshedRegion| class.

In this tutorial, we explore the data about the mesh nodes.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Get the mesh nodes
            nodes_1 = meshed_region_1.nodes

            # Print the object type
            print("Object type: ",type(nodes_1),'\n')

            # Print the nodes
            print("Nodes: ", nodes_1)

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Get the mesh nodes
            nodes_2 = meshed_region_2.nodes

            # Print the object type
            print("Object type: ",type(nodes_2),'\n')

            # Print the nodes
            print("Nodes: ", nodes_2)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Get the mesh nodes
            nodes_3 = meshed_region_3.nodes

            # Print the object type
            print("Object type: ",type(nodes_3),'\n')

            # Print the nodes
            print("Nodes: ", nodes_3)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Get the mesh nodes
            nodes_4 = meshed_region_4.nodes

            # Print the object type
            print("Object type: ",type(nodes_4),'\n')

            # Print the nodes
            print("Nodes: ", nodes_4)

Explore the mesh metadata
-------------------------

You can access the mesh metadata by manipulating the |MeshedRegion| object properties.

The mesh metadata information describes the mesh composition.

You can access which metadata information is available for a given result file.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Get the available properties
            available_props_1 = meshed_region_1.available_property_fields

            # Print the available properties
            print("Available properties: ", available_props_1)

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Get the available properties
            available_props_2 = meshed_region_2.available_property_fields

            # Print the available properties
            print("Available properties: ", available_props_2)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Get the available properties
            available_props_3 = meshed_region_3.available_property_fields

            # Print the available properties
            print("Available properties: ", available_props_3)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Get the available properties
            available_props_4 = meshed_region_4.available_property_fields

            # Print the available properties
            print("Available properties: ", available_props_4)

You can also chose which property you want to extract.

When extracting the properties you get a |PropertyField| with that information. Their data is mapped to
the entity they are defined at.

Here, we extract the element types for the mesh elements.

The element type is given as a number. See the |element_types| to find the
corresponding element name.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Get the element types on the mesh
            el_types_1 = meshed_region_1.property_field(property_name="eltype")

            # Print the element types by element
            print(el_types_1)


    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Get the element types on the mesh
            el_types_2 = meshed_region_2.property_field(property_name="eltype")

            # Print the element types by element
            print(el_types_2)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Get the element types on the mesh
            el_types_3 = meshed_region_3.property_field(property_name="eltype")

            # Print the element types by element
            print(el_types_3)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Get the element types on the mesh
            el_types_4 = meshed_region_4.property_field(property_name="eltype")

            # Print the element types by element
            print(el_types_4)

For more information about how to explore a mesh metadata before extracting it from a result file, see the
:ref:`ref_tutorials_explore_mesh_metadata` tutorial.