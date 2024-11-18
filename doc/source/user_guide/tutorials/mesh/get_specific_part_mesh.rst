.. _tutorials_get_specific_part_mesh:

======================================
Get a mesh split on on different parts
======================================

.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |MeshesContainer| replace:: :class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>`
.. |DataSources| replace:: :class:`Model <ansys.dpf.core.data_sources.DataSources>`
.. |meshes_provider| replace:: :class:`mesh_provider <ansys.dpf.core.operators.mesh.mesh_provider.mesh_provider>`

This tutorial show how to get meshes split on a given space or time

You have one operator that can be used to get your split mesh: |meshes_provider|

Define the |DataSources|
------------------------

The |meshes_provider| operator need a |DataSources| object.

In this part we will download a simulation result file available
in our ``Examples`` package.

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    # Define the result file
    result_file_path2 = examples.download_fluent_axial_comp()["flprj"]
    # Create the DataSources object
    my_data_sources = dpf.DataSources(result_path=result_file_path2)

Use the |meshes_provider| operator
----------------------------------

Instanciate the |meshes_provider| operator.

.. code-block:: python

    # Instanciate the meshes_provider operator
    my_meshes_2 =  ops.mesh.meshes_provider(data_sources=my_data_sources).eval()
    # Print the meshes
    print(my_meshes_2)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    result_file_path2 = examples.download_fluent_axial_comp()["flprj"]
    my_data_sources = dpf.DataSources(result_path=result_file_path2)
    my_meshes_2 =  ops.mesh.meshes_provider(data_sources=my_data_sources).eval()
    print(my_meshes_2)

You can specify the mesh regions you want to get by giving the region id to the ``region_scoping`` argument.
A region corresponds to a zone for Fluid results or a part for LSDyna results.

The given meshes can be spatially or temporally varying, it depends on your result file.

.. code-block:: python

    # Instanciate the meshes_provider operator specifing a region
    my_meshes_3 =  ops.mesh.meshes_provider(data_sources=my_data_sources, region_scoping=[3,12]).eval()
    # Print the meshes
    print(my_meshes_3)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_meshes_3 =  ops.mesh.meshes_provider(data_sources=my_data_sources, region_scoping=[3,12]).eval()
    print(my_meshes_3)

