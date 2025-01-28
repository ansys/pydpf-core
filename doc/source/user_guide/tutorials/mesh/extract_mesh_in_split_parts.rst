.. _ref_tutorials_extract_mesh_in_split_parts:

=============================
Extract a mesh in split parts
=============================

:bdg-fluent:`Fluent` :bdg-cfx:`CFX`

.. include:: ../../../links_and_refs.rst
.. |MeshesContainer| replace:: :class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>`
.. |meshes_provider| replace:: :class:`meshes_provider <ansys.dpf.core.operators.mesh.meshes_provider.meshes_provider>`

This tutorial shows how to extract meshes split on a given space or time from a result file.

To accomplish this goal, you must use the |meshes_provider| operator.

:jupyter-download-script:`Download tutorial as Python script<extract_mesh_in_split_parts>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<extract_mesh_in_split_parts>`

Define the |DataSources|
------------------------

We must create a |DataSources| object so the |meshes_provider| operator can access the mesh. This object
manages paths to their files.

For this tutorial, you can use a result file available in the |Examples| module.
For more information about how to import your own result file in DPF, see the :ref:`ref_tutorials_import_data`
tutorial section.

.. tab-set::

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

Extract the mesh in split parts
-------------------------------

Instanciate and evaluate the |meshes_provider| operator.
The split meshes are given in a |MeshesContainer| and can be spatially or temporally varying.

.. tab-set::

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Instanciate the meshes_provider operator
            meshes_31 =  ops.mesh.meshes_provider(data_sources=ds_3).eval()

            # Print the meshes
            print(meshes_31)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Instanciate the meshes_provider operator
            meshes_41 =  ops.mesh.meshes_provider(data_sources=ds_4).eval()

            # Print the meshes
            print(meshes_41)

Scope the mesh regions to be extracted in split parts
-----------------------------------------------------

A region corresponds to a zone for Fluid and CFX results. You can specify the mesh regions you want to get by giving
the zones ids to the ``region_scoping`` argument.

.. tab-set::

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Instanciate the meshes_provider operator and specify a region
            meshes_32 =  ops.mesh.meshes_provider(data_sources=ds_3, region_scoping=[3,12]).eval()

            # Print the meshes
            print(meshes_32)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Instanciate the meshes_provider operator specifying a region
            meshes_42 =  ops.mesh.meshes_provider(data_sources=ds_4, region_scoping=[5,8]).eval()

            # Print the meshes
            print(meshes_42)
