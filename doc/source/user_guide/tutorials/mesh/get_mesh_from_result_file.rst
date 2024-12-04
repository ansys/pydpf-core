.. _ref_tutorials_get_mesh_from_result_file:

=============================
Get a mesh from a result file
=============================

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

.. include:: ../../../links_and_refs.rst

.. |mesh_provider| replace:: :class:`mesh_provider <ansys.dpf.core.operators.mesh.mesh_provider.mesh_provider>`

This tutorial explains how to extract a mesh from a result file.

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your
own from scratch or by getting it from a result file.

:jupyter-download-script:`Download tutorial as Python script<get_mesh_from_result_file>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<get_mesh_from_result_file>`

Import the result file
----------------------

First, import a result file. For this tutorial, you can use one available in the |Examples| module.
For more information about how to import your own result file in DPF, see the :ref:`ref_tutorials_import_data`
tutorials section.

Here, we create a |DataSources| object so the data can be directly accessed by different
PyDPF-Core APIs. This object manages paths to their files.

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
            # Create the DataSources object
            ds_1 = dpf.DataSources(result_path=result_file_path_1)

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
            # Create the DataSources object
            ds_3 = dpf.DataSources(result_path=result_file_path_3)

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
            # Create the DataSources object
            ds_4 = dpf.DataSources(result_path=result_file_path_4)


Get the mesh from the result file
---------------------------------

You can get the mesh from a result file by two methods:

- :ref:`Using the DPF Model <get_mesh_model>`;
- :ref:`Using the mesh_provider operator <get_mesh_mesh_provider>`.

.. note::

    A |Model| extracts a large amount of information by default (results, mesh and analysis data).
    If using this helper takes a long time for processing the code, mind using a |DataSources| object
    and instantiating operators directly with it.

.. _get_mesh_model:

Using the DPF |Model|
^^^^^^^^^^^^^^^^^^^^^

The |Model| is a helper designed to give shortcuts to access the analysis results
metadata and to instanciate results providers by opening a |DataSources| or a Streams.

Get the |MeshedRegion| by instantiating a |Model| object and accessing its metadata.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Create the Model
            model_1 = dpf.Model(data_sources=ds_1)
            # Get the mesh
            meshed_region_11 = model_1.metadata.meshed_region

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Create the Model
            model_2 = dpf.Model(data_sources=ds_2)
            # Get the mesh
            meshed_region_21 = model_2.metadata.meshed_region

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Create the Model
            model_3 = dpf.Model(data_sources=ds_3)
            # Get the mesh
            meshed_region_31 = model_3.metadata.meshed_region

    .. tab-item:: CFX

        .. jupyter-execute::

            # Create the Model
            model_4 = dpf.Model(data_sources=ds_4)
            # Get the mesh
            meshed_region_41 = model_4.metadata.meshed_region

Printing the |MeshedRegion| displays the mesh dimensions:

- Number of nodes and elements;
- Unit;
- Elements type.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Print the MeshedRegion
            print(meshed_region_11)

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Print the MeshedRegion
            print(meshed_region_21)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Print the MeshedRegion
            print(meshed_region_31)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Print the MeshedRegion
            print(meshed_region_41)

.. _get_mesh_mesh_provider:

Using the |mesh_provider| operator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get the |MeshedRegion| by instantiating the |mesh_provider| operator with the
|DataSources| object as an argument.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Get the mesh with the mesh_provider operator
            meshed_region_12 = ops.mesh.mesh_provider(data_sources=ds_1).eval()

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Get the mesh with the mesh_provider operator
            meshed_region_22 = ops.mesh.mesh_provider(data_sources=ds_2).eval()

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Get the mesh with the mesh_provider operator
            meshed_region_32 = ops.mesh.mesh_provider(data_sources=ds_3).eval()

    .. tab-item:: CFX

        .. jupyter-execute::

            # Get the mesh with the mesh_provider operator
            meshed_region_42 = ops.mesh.mesh_provider(data_sources=ds_4).eval()

Printing the |MeshedRegion| displays the mesh dimensions:

- Number of nodes and elements;
- Unit;
- Elements type.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Print the MeshedRegion
            print(meshed_region_12)

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Print the MeshedRegion
            print(meshed_region_22)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Print the MeshedRegion
            print(meshed_region_32)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Print the MeshedRegion
            print(meshed_region_42)