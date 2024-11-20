.. _ref_tutorials_read_mesh_metadata:

======================
Read the mesh metadata
======================

.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |DataSources| replace:: :class:`Model <ansys.dpf.core.data_sources.DataSources>`
.. |MeshInfo| replace:: :class:`MeshInfo <ansys.dpf.core.mesh_info.MeshInfo>`

This tutorial explains how to read a mesh metadata (data about the elements, nodes, faces, region, zone ...)
for LSDYNA, Fluent or CFX result files.

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your
own by scratch or by getting it from a result file. For more information check the
:ref:`tutorials_create_a_mesh_from_scratch` and :ref:`tutorials_get_mesh_from_result_file` tutorials.

We have the |MeshInfo| object to read metadata information before extracting the |MeshedRegion|.
You can obtain this object by creating a |Model| with a result file.

Define the |Model|
------------------

Here we we will download result files available in our `Examples` package.
For more information about how to import your result file in DPF check
the :ref:`ref_tutorials_import_data` tutorial section.

.. tab-set::

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

Read the mesh metadata
----------------------

The |Model| is a helper designed to give shortcuts to access the analysis results
metadata, by opening a DataSources or a Streams, and to instanciate results provider
for it.

From the |Model| you can access the |MeshedRegion| metadata information with the |MeshInfo| object.
The mesh metadata information includes :

- Properties;
- Parts;
- Faces;
- Bodies;
- Zones;
- Number of nodes and elements;
- Elements types.

Get the the mesh metadata information and print the available ones:

.. tab-set::

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Get the mesh metadata information
            my_mesh_info_2 = my_model_2.metadata.mesh_info
            # Print the mesh metadata information
            print(my_mesh_info_2)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

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
            # Get the mesh metadata information
            my_mesh_info_2 = my_model_2.metadata.mesh_info
            # Print the mesh metadata information
            print(my_mesh_info_2)

    .. tab-item:: Fluent

        .. code-block:: python

            # Get the mesh metadata information
            my_mesh_info_3 = my_model_3.metadata.mesh_info
            # Print the mesh metadata information
            print(my_mesh_info_3)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Define the result file
            result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]
            # Create the model
            my_model_3 = dpf.Model(data_sources=result_file_path_3)
            # Get the mesh
            my_meshed_region_3 = my_model_3.metadata.meshed_region
            # Get the mesh metadata information
            my_mesh_info_3 = my_model_3.metadata.mesh_info
            # Print the mesh metadata information
            print(my_mesh_info_3)

    .. tab-item:: CFX

        .. code-block:: python

            # Get the mesh metadata information
            my_mesh_info_4 = my_model_4.metadata.mesh_info
            # Print the mesh metadata information
            print(my_mesh_info_4)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Define the result file
            result_file_path_4 = examples.download_cfx_mixing_elbow()
            # Create the model
            my_model_4 = dpf.Model(data_sources=result_file_path_4)
            # Get the mesh
            my_meshed_region_4 = my_model_4.metadata.meshed_region
            # Get the mesh metadata information
            my_mesh_info_4 = my_model_4.metadata.mesh_info
            # Print the mesh metadata information
            print(my_mesh_info_4)

You can extract each of those mesh information by manipulating the |MeshInfo| object properties.
For example we can check the part names (for the LSDYNA result file) or the cell zone names
(for the Fluent or CFX result files):

.. tab-set::

    .. tab-item:: LSDYNA

        .. code-block:: python

            # Get the part names
            my_cell_zones_2 = my_mesh_info_2.get_property("part_names")
            print(my_cell_zones_2)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Get the part names
            my_cell_zones_2 = my_mesh_info_2.get_property("part_names")
            print(my_cell_zones_2)

    .. tab-item:: Fluent

        .. code-block:: python

            # Get the cell zone names
            my_cell_zones_3 = my_mesh_info_3.get_property("cell_zone_names")
            print(my_cell_zones_3)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Get the cell zone names
            my_cell_zones_3 = my_mesh_info_3.get_property("cell_zone_names")
            print(my_cell_zones_3)

    .. tab-item:: CFX

        .. code-block:: python

            # Get the cell zone names
            my_cell_zones_4 = my_mesh_info_4.get_property("cell_zone_names")
            print(my_cell_zones_4)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Get the cell zone names
            my_cell_zones_4 = my_mesh_info_4.get_property("cell_zone_names")
            print(my_cell_zones_4)

For more information on reading a mesh from a LSDYNA, Fluent or CFX file check the examples sections:
:ref:`examples_lsdyna`, :ref:`fluids_examples` and :ref:`examples_cfx`.