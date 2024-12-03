.. _tutorials_split_mesh:

============
Split a mesh
============

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

This tutorial show how to split a mesh into different meshes.

.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |MeshesContainer| replace:: :class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>`
.. |split_mesh| replace:: :class:`split_mesh <ansys.dpf.core.operators.mesh.split_mesh.split_mesh>`
.. |split_on_property_type| replace:: :class:`split_on_property_type <ansys.dpf.core.operators.scoping.split_on_property_type.split_on_property_type>`
.. |from_scopings| replace:: :class:`from_scopings <ansys.dpf.core.operators.mesh.from_scopings.from_scopings>`
.. |DataSources| replace:: :class:`Model <ansys.dpf.core.data_sources.DataSources>`
.. |Scoping| replace:: :class:`Scoping <ansys.dpf.core.scoping.Scoping>`
.. |ScopingsContainer| replace:: :class:`ScopingsContainer <ansys.dpf.core.scopings_container.ScopingsContainer>`
.. |Examples| replace:: :mod:`Examples<ansys.dpf.core.examples>`

The mesh object in DPF is a |MeshedRegion|. If you want to split your mesh you can store them in a |MeshedRegion|.

You have two approaches to split your mesh:

1) Using the |split_mesh|, to split a already existing |MeshedRegion| into a MeshesContainer;
2) Split the scoping with the |split_on_property_type| operator and than creating the |MeshedRegion|
   objects with the |from_scopings| operator.

Define the mesh
---------------

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your
own by scratch or by getting it from a result file. For more information check the
:ref:`tutorials_create_a_mesh_from_scratch` and :ref:`tutorials_get_mesh_from_result_file` tutorials.

In this part we will download simulation result files available
in our |Examples| package.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

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
            # Create the model
            my_model_2 = dpf.Model(data_sources=my_data_sources_2)
            # Get the mesh
            my_meshed_region_2 = my_model_2.metadata.meshed_region

    .. tab-item:: Fluent

        .. jupyter-execute::

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

        .. jupyter-execute::

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

1) First approach
-----------------

Use the |split_mesh| operator to split a already existing |MeshedRegion| into a MeshesContainer based on a property.
Currently you can split a mesh by material or eltype.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Split the mesh by material
            my_meshes_11 = ops.mesh.split_mesh(mesh=my_meshed_region_1,property="mat").eval()
            # Print the meshes
            print(my_meshes_11)

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Split the mesh by material
            my_meshes_21 = ops.mesh.split_mesh(mesh=my_meshed_region_2,property="mat").eval()
            # Print the meshes
            print(my_meshes_21)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Split the mesh by material
            my_meshes_31 = ops.mesh.split_mesh(mesh=my_meshed_region_3,property="mat").eval()
            # Print the meshes
            print(my_meshes_31)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Split the mesh by material
            my_meshes_41 = ops.mesh.split_mesh(mesh=my_meshed_region_4,property="mat").eval()
            # Print the meshes
            print(my_meshes_41)


2) Second approach
------------------

Use the |split_on_property_type| operator to split the scoping and then create the |MeshedRegion|
objects with the |from_scopings| operator.

The |split_on_property_type| a given |Scoping| on given properties (elshape and/or material, since 2025R1
it supports any scalar property field name contained in the mesh property fields) and returns a |ScopingsContainer|
with those split scopings.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Define the scoping split by material
            split_scoping_1 = ops.scoping.split_on_property_type(mesh=my_meshed_region_1, label1="mat").eval()
            # Get the split meshes
            my_meshes_12 = ops.mesh.from_scopings(scopings_container=split_scoping_1,mesh=my_meshed_region_1).eval()
            # Print the meshes
            print(my_meshes_12)

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Define the scoping split by material
            split_scoping_2 = ops.scoping.split_on_property_type(mesh=my_meshed_region_2, label1="mat").eval()
            # Get the split meshes
            my_meshes_22 = ops.mesh.from_scopings(scopings_container=split_scoping_2,mesh=my_meshed_region_2).eval()
            # Print the meshes
            print(my_meshes_22)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Define the scoping split by material
            split_scoping_3 = ops.scoping.split_on_property_type(mesh=my_meshed_region_3, label1="mat").eval()
            # Get the split meshes
            my_meshes_32 = ops.mesh.from_scopings(scopings_container=split_scoping_3,mesh=my_meshed_region_3).eval()
            # Print the meshes
            print(my_meshes_32)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Define the scoping split by material
            split_scoping_4 = ops.scoping.split_on_property_type(mesh=my_meshed_region_4, label1="mat").eval()
            # Get the split meshes
            my_meshes_42 = ops.mesh.from_scopings(scopings_container=split_scoping_4,mesh=my_meshed_region_4).eval()
            # Print the meshes
            print(my_meshes_42)
