.. _ref_tutorials_explore_mesh_metadata:

=======================
Explore a mesh metadata
=======================

:bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

.. include:: ../../../links_and_refs.rst
.. |PropertyField| replace:: :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`
.. |StringField| replace:: :class:`StringField <ansys.dpf.core.string_field.StringField>`

This tutorial explains how to read a mesh metadata (data about the elements, nodes, faces, region, zone ...)
before extracting the mesh from a result file.

:jupyter-download-script:`Download tutorial as Python script<read_mesh_metadata>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<read_mesh_metadata>`

Get the result file
-------------------

First, import a result file. For this tutorial, you can use one available in the |Examples| module.
For more information about how to import your own result file in DPF, see the :ref:`ref_tutorials_import_data`
tutorial section.

.. tab-set::

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module
            from ansys.dpf import core as dpf
            # Import the examples module
            from ansys.dpf.core import examples

            # Define the result file path
            result_file_path_2 = examples.download_d3plot_beam()

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module
            from ansys.dpf import core as dpf
            # Import the examples module
            from ansys.dpf.core import examples

            # Define the result file path
            result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]

    .. tab-item:: CFX

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module
            from ansys.dpf import core as dpf
            # Import the examples module
            from ansys.dpf.core import examples

            # Define the result file path
            result_file_path_4 = examples.download_cfx_mixing_elbow()

Create the |Model|
------------------

Create a |Model| object with the result file. The |Model| is a helper designed to give shortcuts to
access the analysis results metadata and to instanciate results providers by opening a |DataSources| or a Streams.

.. tab-set::

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Create the DataSources object
            ds_2 = dpf.DataSources()
            ds_2.set_result_file_path(filepath=result_file_path_2[0], key="d3plot")
            ds_2.add_file_path(filepath=result_file_path_2[3], key="actunits")
            # Create the Model
            model_2 = dpf.Model(data_sources=ds_2)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Create the Model
            model_3 = dpf.Model(data_sources=result_file_path_3)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Create the Model
            model_4 = dpf.Model(data_sources=result_file_path_4)

Explore the mesh metadata
-------------------------

You can access the mesh metadata with the |MeshInfo| object. It reads the metadata information before extracting
the |MeshedRegion| from the result file.

The mesh metadata information is stored in a |PropertyField| or in a |StringField|. They contain information
that describes the mesh composition and their data is mapped to the entity they are defined at.
The mesh metadata information information can be:

- Properties;
- Parts;
- Faces;
- Bodies;
- Zones;
- Number of nodes and elements;
- Elements types.

You can access which metadata information is available for a given result file.

.. tab-set::

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Get the mesh metadata information
            mesh_info_2 = model_2.metadata.mesh_info

            # Print the mesh metadata information
            print(mesh_info_2)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Get the mesh metadata information
            mesh_info_3 = model_3.metadata.mesh_info

            # Print the mesh metadata information
            print(mesh_info_3)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Get the mesh metadata information
            mesh_info_4 = model_4.metadata.mesh_info

            # Print the mesh metadata information
            print(mesh_info_4)

You can also extract each of those mesh metadata information by manipulating the |MeshInfo| object properties.

For example, we can check the part names (for the LSDYNA result file) or the cell zone names
(for the Fluent or CFX result files):

.. tab-set::

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Get the part names
            cell_zones_2 = mesh_info_2.get_property("part_names")

            # Print the part names
            print(cell_zones_2)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Get the cell zone names
            cell_zones_3 = mesh_info_3.get_property("cell_zone_names")

            # Print the cell zone names
            print(cell_zones_3)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Get the cell zone names
            cell_zones_4 = mesh_info_4.get_property("cell_zone_names")

            # Print the cell zone names
            print(cell_zones_4)

For more information on reading a mesh from a LSDYNA, Fluent or CFX file check the :ref:`examples_lsdyna`,
:ref:`fluids_examples` and :ref:`examples_cfx` examples sections.