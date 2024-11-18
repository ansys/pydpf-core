.. _tutorials_split_mesh:

============
Split a mesh
============

This tutorial show how to split a mesh into different meshes.

.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |MeshesContainer| replace:: :class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>`
.. |split_mesh| replace:: :class:`split_mesh <ansys.dpf.core.operators.mesh.split_mesh.split_mesh>`

The mesh object in DPF is a |MeshedRegion|. If you want to split your mesh you can store them in a |MeshesContainer|.

You have one operator that can be used to split your mesh: |split_mesh|

Define the mesh
---------------

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your
own by scratch or by getting it from a result file. For more information check the
:ref:`tutorials_create_a_mesh_from_scratch` and :ref:`tutorials_get_mesh_from_result_file` tutorials.

In this part we will download a simulation result file available
in our ``Examples`` package.

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    # Define the result file
    result_file_path_1 = examples.find_multishells_rst()
    # Create the model
    my_model_1 = dpf.Model(data_sources=result_file_path_1)
    # Get the mesh
    my_meshed_region_1 = my_model_1.metadata.meshed_region


Use the |split_mesh| operator
-----------------------------

The |split_mesh| operator divides a |MeshedRegion| based on a property.
Currently you can split a mesh by material or eltype.

.. code-block:: python

    # Split the mesh by material
    my_meshes_1 = ops..mesh.split_mesh(mesh=my_meshed_region_1,property="mat").eval()
    # Print the meshes
    print(my_meshes_1)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    result_file_path_1 = examples.find_multishells_rst()
    my_model_1 = dpf.Model(data_sources=result_file_path_1)
    my_meshed_region_1 = my_model_1.metadata.meshed_region
    my_meshes_1 = ops.mesh.split_mesh(mesh=my_meshed_region_1,property="mat").eval()
    print(my_meshes_1)
