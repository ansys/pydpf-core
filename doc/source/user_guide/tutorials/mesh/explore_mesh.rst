.. _tutorials_explore_mesh:

==============
Explore a mesh
==============

.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |DataSources| replace:: :class:`Model <ansys.dpf.core.data_sources.DataSources>`
.. |MeshInfo| replace:: :class:`MeshInfo <ansys.dpf.core.mesh_info.MeshInfo>`
.. |Nodes| replace:: :class:`Nodes <ansys.dpf.core.nodes.Nodes>`
.. |Elements| replace:: :class:`Elements <ansys.dpf.core.elements.Elements>`
.. |Faces| replace:: :class:`Faces <ansys.dpf.core.faces.Faces>`
.. |Scoping| replace:: :class:`Scoping <ansys.dpf.core.scoping.Scoping>`
.. |PropertyField| replace:: :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`

This tutorial explains how to access the mesh data and metadata (data about the elements, nodes, faces, region, zone ...)
so it can be manipulated.

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your
own by scratch or by getting it from a result file. For more information check the
:ref:`tutorials_create_a_mesh_from_scratch` and :ref:`tutorials_get_mesh_from_result_file` tutorials.

There is a general method to read the |MeshedRegion| by manipulating
the methods of this object.

Define the mesh
---------------

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your
own by scratch or by getting it from a result file. For more information check the
:ref:`tutorials_create_a_mesh_from_scratch` and :ref:`tutorials_get_mesh_from_result_file` tutorials.

Here we we will download a  result file available in our `Examples` package.
For more information about how to import your result file in DPF check
the :ref:`ref_tutorials_import_data` tutorial section.

.. tab-set::

    .. tab-item:: MAPDL


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

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops
            # Define the result file
            result_file_path_2 = examples.download_d3plot_beam()
            # Create the DataSources object
            my_data_sources_2 = dpf.DataSources()
            my_data_sources_2.set_result_file_path(filepath=result_file_path_2[0], key="d3plot")
            my_data_sources_2.add_file_path(filepath=result_file_path_2[3], key="actunits")
            # Create the model
            my_model_2 = dpf.Model(data_sources=my_data_sources_2)
            # Get the mesh
            my_meshed_region_2 = my_model_2.metadata.meshed_region

    .. tab-item:: Fluent

        .. code-block:: python

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops
            # Define the result file
            result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]
            # Create the model
            my_model_3 = dpf.Model(data_sources=result_file_path_3)
            # Get the mesh
            my_meshed_region_3 = my_model_3.metadata.meshed_region

    .. tab-item:: CFX

        .. code-block:: python

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops
            # Define the result file
            result_file_path_4 = examples.download_cfx_mixing_elbow()
            # Create the model
            my_model_4 = dpf.Model(data_sources=result_file_path_4)
            # Get the mesh
            my_meshed_region_4 = my_model_4.metadata.meshed_region

Read the mesh
-------------

From the |MeshedRegion| you can access its information by manipulating this object properties.
The mesh information includes :

- Unit;
- Nodes, elements and faces;
- Named selections;
- Properties.

Check all the information you can get at: |MeshedRegion|.

Access the mesh nodes, element, faces and named selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When instantiating the nodes, element, faces and named selection you get the correspondent DPF objects:
|Nodes|, |Elements|, |Faces| and |Scoping|. For example:

.. tab-set::

    .. tab-item:: MAPDL

        .. code-block:: python

            # Get the mesh elements
            my_nodes_1 = my_meshed_region_1.nodes
            # Print the nodes
            print(my_nodes_1)
            print("Object type: ",type(my_nodes_1))

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

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
            # Get the mesh elements
            my_nodes_1 = my_meshed_region_1.nodes
            # Print the nodes
            print(my_nodes_1)
            print("Object type: ",type(my_nodes_1))

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Get the mesh elements
            my_nodes_2 = my_meshed_region_2.nodes
            # Print the nodes
            print(my_nodes_2)
            print("Object type: ",type(my_nodes_2))

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Define the result file
            result_file_path_2 = examples.download_d3plot_beam()
            # Create the DataSources object
            my_data_sources_2 = dpf.DataSources()
            my_data_sources_2.set_result_file_path(filepath=result_file_path_2[0], key="d3plot")
            my_data_sources_2.add_file_path(filepath=result_file_path_2[3], key="actunits")
            # Create the model
            my_model_2 = dpf.Model(data_sources=my_data_sources_2)
            # Get the mesh
            my_meshed_region_2 = my_model_2.metadata.meshed_region
            # Get the mesh elements
            my_nodes_2 = my_meshed_region_2.nodes
            # Print the nodes
            print(my_nodes_2)
            print("Object type: ",type(my_nodes_2))

    .. tab-item:: Fluent

        .. code-block:: python

            # Get the mesh elements
            my_nodes_3 = my_meshed_region_3.nodes
            # Print the nodes
            print(my_nodes_3)
            print("Object type: ",type(my_nodes_3))

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Define the result file
            result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]
            # Create the model
            my_model_3 = dpf.Model(data_sources=result_file_path_3)
            # Get the mesh
            my_meshed_region_3 = my_model_3.metadata.meshed_region
            # Get the mesh elements
            my_nodes_3 = my_meshed_region_3.nodes
            # Print the nodes
            print(my_nodes_3)
            print("Object type: ",type(my_nodes_3))

    .. tab-item:: CFX

        .. code-block:: python

            # Get the mesh elements
            my_nodes_4 = my_meshed_region_4.nodes
            # Print the nodes
            print(my_nodes_4)
            print("Object type: ",type(my_nodes_4))

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Define the result file
            result_file_path_4 = examples.download_cfx_mixing_elbow()
            # Create the model
            my_model_4 = dpf.Model(data_sources=result_file_path_4)
            # Get the mesh
            my_meshed_region_4 = my_model_4.metadata.meshed_region
            # Get the mesh elements
            my_nodes_4 = my_meshed_region_4.nodes
            # Print the nodes
            print(my_nodes_4)
            print("Object type: ",type(my_nodes_4))

Access the mesh properties
^^^^^^^^^^^^^^^^^^^^^^^^^^

When handling properties you can check which are the available ones and also
chose those you want to extract.

.. tab-set::

    .. tab-item:: MAPDL

        .. code-block:: python

            # Get the available properties
            my_available_props_1 = my_meshed_region_1.available_property_fields
            # Print the available properties
            print(my_available_props_1)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Get the available properties
            my_available_props_1 = my_meshed_region_1.available_property_fields
            # Print the available properties
            print(my_available_props_1)

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Get the available properties
            my_available_props_2 = my_meshed_region_2.available_property_fields
            # Print the available properties
            print(my_available_props_2)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Get the available properties
            my_available_props_2 = my_meshed_region_2.available_property_fields
            # Print the available properties
            print(my_available_props_2)

    .. tab-item:: Fluent

        .. code-block:: python

            # Get the available properties
            my_available_props_3 = my_meshed_region_3.available_property_fields
            # Print the available properties
            print(my_available_props_3)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Get the available properties
            my_available_props_3 = my_meshed_region_3.available_property_fields
            # Print the available properties
            print(my_available_props_3)

    .. tab-item:: CFX

        .. code-block:: python

            # Get the available properties
            my_available_props_4 = my_meshed_region_4.available_property_fields
            # Print the available properties
            print(my_available_props_4)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Get the available properties
            my_available_props_4 = my_meshed_region_4.available_property_fields
            # Print the available properties
            print(my_available_props_4)

When extracting those properties you get a |PropertyField| with that information. Their data is mapped
to the entity they are defined at:

.. tab-set::

    .. tab-item:: MAPDL

        .. code-block:: python

            # Get the element types on the mesh
            my_el_types_1 = my_meshed_region_1.property_field(property_name="eltype")
            # Print the element types
            print(my_el_types_1)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Get the element types on the mesh
            my_el_types_1 = my_meshed_region_1.property_field(property_name="eltype")
            # Print the element types
            print(my_el_types_1)


    .. tab-item:: LSDYNA

        .. code-block:: python

            # Get the element types on the mesh
            my_el_types_2 = my_meshed_region_2.property_field(property_name="eltype")
            # Print the element types
            print(my_el_types_2)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Get the element types on the mesh
            my_el_types_2 = my_meshed_region_2.property_field(property_name="eltype")
            # Print the element types
            print(my_el_types_2)


    .. tab-item:: Fluent

        .. code-block:: python

            # Get the element types on the mesh
            my_el_types_3 = my_meshed_region_3.property_field(property_name="eltype")
            # Print the element types
            print(my_el_types_3)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Get the element types on the mesh
            my_el_types_3 = my_meshed_region_3.property_field(property_name="eltype")
            # Print the element types
            print(my_el_types_3)

    .. tab-item:: CFX

        .. code-block:: python

            # Get the element types on the mesh
            my_el_types_4 = my_meshed_region_4.property_field(property_name="eltype")
            # Print the element types
            print(my_el_types_4)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Get the element types on the mesh
            my_el_types_4 = my_meshed_region_4.property_field(property_name="eltype")
            # Print the element types
            print(my_el_types_4)