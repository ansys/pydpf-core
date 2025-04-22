.. _ref_tutorials_split_mesh:

============
Split a mesh
============

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LSDYNA` :bdg-fluent:`Fluent` :bdg-cfx:`CFX`

.. include:: ../../../links_and_refs.rst

.. |MeshesContainer| replace:: :class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>`
.. |split_mesh| replace:: :class:`split_mesh <ansys.dpf.core.operators.mesh.split_mesh.split_mesh>`
.. |split_on_property_type| replace:: :class:`split_on_property_type <ansys.dpf.core.operators.scoping.split_on_property_type.split_on_property_type>`
.. |from_scopings| replace:: :class:`from_scopings <ansys.dpf.core.operators.mesh.from_scopings.from_scopings>`
.. |ScopingsContainer| replace:: :class:`ScopingsContainer <ansys.dpf.core.scopings_container.ScopingsContainer>`
.. |PropertyField| replace:: :class:`PropertyField <ansys.dpf.core.property_field.PropertyField>`

This tutorial shows how to split a mesh on a give property.

There are two approaches to accomplish this goal:

- :ref:`Use the split_mesh operator to split a already existing MeshedRegion<ref_first_approach_split_mesh>`;
- :ref:`Split the mesh scoping and create the split MeshedRegion objects <ref_second_approach_split_mesh>`.

:jupyter-download-script:`Download tutorial as Python script<split_mesh>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<split_mesh>`

Define the mesh
---------------

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your own from scratch or by getting it from a result file. For more
information check the :ref:`ref_tutorials_create_a_mesh_from_scratch` and :ref:`ref_tutorials_get_mesh_from_result_file`
tutorials.

For this tutorial, we get a |MeshedRegion| from a result file. You can use one available in the |Examples| module.
For more information see the :ref:`ref_tutorials_get_mesh_from_result_file` tutorial.

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
            result_file_path_1 = examples.find_multishells_rst()
            # Create the model
            model_1 = dpf.Model(data_sources=result_file_path_1)
            # Get the mesh
            meshed_region_1 = model_1.metadata.meshed_region

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
            # Create the model
            model_2 = dpf.Model(data_sources=ds_2)
            # Get the mesh
            meshed_region_2 = model_2.metadata.meshed_region

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
            # Create the model
            model_3 = dpf.Model(data_sources=result_file_path_3)
            # Get the mesh
            meshed_region_3 = model_3.metadata.meshed_region

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
            # Create the model
            model_4 = dpf.Model(data_sources=result_file_path_4)
            # Get the mesh
            meshed_region_4 = model_4.metadata.meshed_region

.. _ref_first_approach_split_mesh:

First approach
--------------

This approach consist of splitting an already existing |MeshedRegion| based on a given property. To accomplish
that goal, you must use the |split_mesh| operator. Currently you can split a mesh by material or eltype.

The split mesh parts are stored in the DPF collection called |MeshesContainer|, where they are ordered by *labels*.
When you use the |split_mesh| operator, each split mesh part has two different *labels*:

- A "body" *label*;
- A *label* with the property used to split the mesh.

Here, we split the |MeshedRegion| by material.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Split the mesh by material
            meshes_11 = ops.mesh.split_mesh(mesh=meshed_region_1,property="mat").eval()

            # Print the meshes
            print(meshes_11)

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Split the mesh by material
            meshes_21 = ops.mesh.split_mesh(mesh=meshed_region_2,property="mat").eval()

            # Print the meshes
            print(meshes_21)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Split the mesh by material
            meshes_31 = ops.mesh.split_mesh(mesh=meshed_region_3,property="mat").eval()

            # Print the meshes
            print(meshes_31)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Split the mesh by material
            meshes_41 = ops.mesh.split_mesh(mesh=meshed_region_4,property="mat").eval()
            # Print the meshes
            print(meshes_41)

.. _ref_second_approach_split_mesh:

Second approach
---------------

This approach consists of splitting the |Scoping| of a given |MeshedRegion| based on a given property and then creating
a new |MeshedRegion| for each split |Scoping|.

To accomplish this goal you must follow these steps:

#. Use the |split_on_property_type| operator to split the mesh |Scoping|.
    This operator splits a |Scoping| on a given property (elshape and/or material, since 2025R1 it supports any
    scalar property field name contained in the mesh property fields). The split |Scoping| is stored in the DPF
    collection called |ScopingsContainer|, where they are ordered by *labels*. In this case, you get *labels* with
    the property used to split the |Scoping|.

#. Create the split |MeshedRegion| objects using the |from_scopings| operator for the |Scoping| of interest.
    The split parts are stored in the DPF collection called |MeshesContainer| where they are also ordered by *labels*.
    These *labels* are corresponding to the "mat" labels gotten with the |split_on_property_type| operator.

Here, we split the mesh scoping by material and create a |MeshedRegion| for all the split |Scoping| in the
|ScopingsContainer|.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Define the scoping split by material
            split_scoping_1 = ops.scoping.split_on_property_type(mesh=meshed_region_1, label1="mat").eval()
            # Get the split meshes
            meshes_12 = ops.mesh.from_scopings(scopings_container=split_scoping_1,mesh=meshed_region_1).eval()
            # Print the meshes
            print(meshes_12)

    .. tab-item:: LSDYNA

        .. jupyter-execute::

            # Define the scoping split by material
            split_scoping_2 = ops.scoping.split_on_property_type(mesh=meshed_region_2, label1="mat").eval()
            # Get the split meshes
            meshes_22 = ops.mesh.from_scopings(scopings_container=split_scoping_2,mesh=meshed_region_2).eval()
            # Print the meshes
            print(meshes_22)

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Define the scoping split by material
            split_scoping_3 = ops.scoping.split_on_property_type(mesh=meshed_region_3, label1="mat").eval()
            # Get the split meshes
            meshes_32 = ops.mesh.from_scopings(scopings_container=split_scoping_3,mesh=meshed_region_3).eval()
            # Print the meshes
            print(meshes_32)

    .. tab-item:: CFX

        .. jupyter-execute::

            # Define the scoping split by material
            split_scoping_4 = ops.scoping.split_on_property_type(mesh=meshed_region_4, label1="mat").eval()
            # Get the split meshes
            meshes_42 = ops.mesh.from_scopings(scopings_container=split_scoping_4,mesh=meshed_region_4).eval()
            # Print the meshes
            print(meshes_42)
