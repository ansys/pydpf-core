.. _tutorials_get_mesh_from_result_file:

=============================
Get a mesh from a result file
=============================

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`
.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |DataSources| replace:: :class:`Model <ansys.dpf.core.data_sources.DataSources>`
.. |mesh_provider| replace:: :class:`mesh_provider <ansys.dpf.core.operators.mesh.mesh_provider.mesh_provider>`
.. |Examples| replace:: :mod:`Examples<ansys.dpf.core.examples>`

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your
own by scratch or by getting it from a result file.

This tutorial explains how to extract the models mesh from a result file.


Import the result file
----------------------

Here we we will download result files available in our |Examples| package.
For more information about how to import your result file in DPF check
the :ref:`ref_tutorials_import_data` tutorial section.

You have to create a |DataSources| object so the data can be accessed by
PyDPF-Core APIs.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops
            # Define the result file
            result_file_path_1 = examples.find_static_rst()
            # Create the DataSources object
            my_data_sources_1 = dpf.DataSources(result_path=result_file_path_1)

    .. tab-item:: LSDYNA

        .. jupyter-execute::

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

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops
            # Define the result file
            result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]
            # Create the DataSources object
            my_data_sources_3 = dpf.DataSources(result_path=result_file_path_3)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops
            # Define the result file
            result_file_path_4 = examples.download_cfx_mixing_elbow()
            # Create the DataSources object
            my_data_sources_4 = dpf.DataSources(result_path=result_file_path_4)


Get the mesh from the result file
---------------------------------

You can Get the mesh from the result file by two methods:

- :ref:`get_mesh_model`
- :ref:`get_mesh_mesh_provider`

.. note::

    The |Model| extracts a large amount of information by default (results, mesh and analysis data).
    If using this helper takes a long time for processing the code, mind using a |DataSources| object
    and instantiating operators directly with it. Check the ":ref:`get_mesh_mesh_provider`" for more
    information on how to get a mesh from a result file.

.. _get_mesh_model:

Using the DPF |Model|
^^^^^^^^^^^^^^^^^^^^^

The |Model| is a helper designed to give shortcuts to access the analysis results
metadata, by opening a DataSources or a Streams, and to instanciate results provider
for it.

Get the |MeshedRegion| by instantiating a |Model| object and accessing its metadata:

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Create the model
            my_model_1 = dpf.Model(data_sources=my_data_sources_1)
            # Get the mesh
            my_meshed_region_1 = my_model_1.metadata.meshed_region

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Create the model
            my_model_2 = dpf.Model(data_sources=my_data_sources_2)
            # Get the mesh
            my_meshed_region_2 = my_model_2.metadata.meshed_region

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Create the model
            my_model_3 = dpf.Model(data_sources=my_data_sources_3)
            # Get the mesh
            my_meshed_region_3 = my_model_3.metadata.meshed_region

    .. tab-item:: CFX

        .. jupyter-execute::

            # Create the model
            my_model_4 = dpf.Model(data_sources=my_data_sources_4)
            # Get the mesh
            my_meshed_region_4 = my_model_4.metadata.meshed_region

Printing the |MeshedRegion| displays the mesh dimensions (number of nodes and elements,
unit and elements type):

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Print the meshed region
            print(my_meshed_region_1)

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Print the meshed region
            print(my_meshed_region_2)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Print the meshed region
            print(my_meshed_region_3)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Print the meshed region
            print(my_meshed_region_4)

.. _get_mesh_mesh_provider:

Using the |mesh_provider| operator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get the |MeshedRegion| by instantiating the |mesh_provider| operator and instantiating it with a
|DataSources| object as an argument:

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Get the mesh with the mesh_provider operator
            my_meshed_region_12 = ops.mesh.mesh_provider(data_sources=my_data_sources_1).eval()

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Get the mesh with the mesh_provider operator
            my_meshed_region_22 = ops.mesh.mesh_provider(data_sources=my_data_sources_2).eval()

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Get the mesh with the mesh_provider operator
            my_meshed_region_32 = ops.mesh.mesh_provider(data_sources=my_data_sources_3).eval()

    .. tab-item:: CFX

        .. jupyter-execute::

            # Get the mesh with the mesh_provider operator
            my_meshed_region_42 = ops.mesh.mesh_provider(data_sources=my_data_sources_4).eval()

Printing the |MeshedRegion| displays the mesh dimensions (number of nodes and elements,
unit and elements type):

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Print the meshed region
            print(my_meshed_region_12)

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Print the meshed region
            print(my_meshed_region_22)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Print the meshed region
            print(my_meshed_region_32)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Print the meshed region
            print(my_meshed_region_42)