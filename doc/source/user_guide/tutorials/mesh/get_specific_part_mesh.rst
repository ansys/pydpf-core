.. _tutorials_get_specific_part_mesh:

===================================
Get a mesh split on different parts
===================================

:bdg-info:`Fluent` :bdg-light:`CFX`

.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |MeshesContainer| replace:: :class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>`
.. |DataSources| replace:: :class:`Model <ansys.dpf.core.data_sources.DataSources>`
.. |meshes_provider| replace:: :class:`mesh_provider <ansys.dpf.core.operators.mesh.mesh_provider.mesh_provider>`

This tutorial show how to get meshes split on a given space or time for Fluent or CFX result files.

You have one operator in this case: |meshes_provider|

Define the |DataSources|
------------------------

The |meshes_provider| operator needs a |DataSources| object.

In this part we will download simulation result files available
in our ``Examples`` package.

.. tab-set::

    .. tab-item:: Fluent

        .. code-block:: python

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops
            # Define the result file
            result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]
            # Create the DataSources object
            my_data_sources_3 = dpf.DataSources(result_path=result_file_path_3)

    .. tab-item:: CFX

        .. code-block:: python

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops
            # Define the result file
            result_file_path_4 = examples.download_cfx_mixing_elbow()
            # Create the DataSources object
            my_data_sources_4 = dpf.DataSources(result_path=result_file_path_4)

Use the |meshes_provider| operator
----------------------------------

Instanciate the |meshes_provider| operator.

.. tab-set::

    .. tab-item:: Fluent

        .. code-block:: python

            # Instanciate the meshes_provider operator
            my_meshes_31 =  ops.mesh.meshes_provider(data_sources=my_data_sources_3).eval()
            # Print the meshes
            print(my_meshes_31)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
            from ansys.dpf import core as dpf
            from ansys.dpf.core import examples
            from ansys.dpf.core import operators as ops
            # Define the result file
            result_file_path_3 = examples.download_fluent_axial_comp()["flprj"]
            # Create the DataSources object
            my_data_sources_3 = dpf.DataSources(result_path=result_file_path_3)
            # Instanciate the meshes_provider operator
            my_meshes_31 =  ops.mesh.meshes_provider(data_sources=my_data_sources_3).eval()
            # Print the meshes
            print(my_meshes_31)

    .. tab-item:: CFX

        .. code-block:: python

            # Instanciate the meshes_provider operator
            my_meshes_41 =  ops.mesh.meshes_provider(data_sources=my_data_sources_4).eval()
            # Print the meshes
            print(my_meshes_41)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Define the result file
            result_file_path_4 = examples.download_cfx_mixing_elbow()
            # Create the DataSources object
            my_data_sources_4 = dpf.DataSources(result_path=result_file_path_4)
            # Instanciate the meshes_provider operator
            my_meshes_41 =  ops.mesh.meshes_provider(data_sources=my_data_sources_4).eval()
            # Print the meshes
            print(my_meshes_41)

Scope the regions to be extracted
---------------------------------

You can specify the mesh regions you want to get by giving the region id to the ``region_scoping`` argument.
A region corresponds to a zone for Fluid results.

The given meshes can be spatially or temporally varying, it depends on your result file.

.. tab-set::

    .. tab-item:: Fluent

        .. code-block:: python

            # Instanciate the meshes_provider operator and specify a region
            my_meshes_32 =  ops.mesh.meshes_provider(data_sources=my_data_sources_3, region_scoping=[3,12]).eval()
            # Print the meshes
            print(my_meshes_32)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Instanciate the meshes_provider operator specifying a region
            my_meshes_32 =  ops.mesh.meshes_provider(data_sources=my_data_sources_3, region_scoping=[3,12]).eval()
            # Print the meshes
            print(my_meshes_32)

    .. tab-item:: CFX

        .. code-block:: python

            # Instanciate the meshes_provider operator specifying a region
            my_meshes_42 =  ops.mesh.meshes_provider(data_sources=my_data_sources_4, region_scoping=[5,8]).eval()
            # Print the meshes
            print(my_meshes_42)

        .. rst-class:: sphx-glr-script-out

         .. jupyter-execute::
            :hide-code:

            # Instanciate the meshes_provider operator specifying a region
            my_meshes_42 =  ops.mesh.meshes_provider(data_sources=my_data_sources_4, region_scoping=[5,8]).eval()
            # Print the meshes
            print(my_meshes_42)
