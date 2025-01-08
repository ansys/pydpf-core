.. _ref_tutorials_plot_deformed_mesh:

====================
Plot a deformed mesh
====================

.. |Model.plot| replace:: :func:`Model.plot()<ansys.dpf.core.model.Model.plot>`
.. |MeshedRegion.plot| replace:: :func:`MeshedRegion.plot() <ansys.dpf.core.meshed_region.MeshedRegion.plot>`
.. |MeshesContainer.plot| replace:: :func:`MeshesContainer.plot()<ansys.dpf.core.meshes_container.MeshesContainer.plot>`
.. |add_mesh| replace:: :func:`add_mesh()<ansys.dpf.core.plotter.DpfPlotter.add_mesh>`
.. |show_figure| replace:: :func:`show_figure()<ansys.dpf.core.plotter.DpfPlotter.show_figure>`
.. |split_mesh| replace:: :class:`split_mesh <ansys.dpf.core.operators.mesh.split_mesh.split_mesh>`

This tutorial shows different plotting commands to plot the bare deformed mesh
of a model.

DPF-Core has a variety of plotting methods for generating 3D plots of
Ansys models directly from Python. These methods use VTK and leverage
the `PyVista <pyVista_github_>`_ library to simplify plotting.

:jupyter-download-script:`Download tutorial as Python script<plot_deformed_mesh>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<plot_deformed_mesh>`

Define the mesh
---------------

The mesh object in DPF is a |MeshedRegion|. You can store multiple |MeshedRegion| in a DPF collection
called |MeshesContainer|.

You can obtain a |MeshedRegion| by creating your own from scratch or by getting it from a result file.
For more information, see the :ref:`ref_tutorials_create_a_mesh_from_scratch` and
:ref:`ref_tutorials_get_mesh_from_result_file` tutorials.

For this tutorial, we get a |MeshedRegion| from a result file. You can use one available in the |Examples| module.
For more information see the :ref:`ref_tutorials_get_mesh_from_result_file` tutorial.

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module
    from ansys.dpf import core as dpf
    # Import the examples module
    from ansys.dpf.core import examples
    # Import the operators module
    from ansys.dpf.core import operators as ops

    # Define the result file path
    result_file_path_1 = examples.find_multishells_rst()

    # Define the DataSources
    ds_1 = dpf.DataSources(result_path=result_file_path_1)

    # Create a model
    model_1 = dpf.Model(data_sources=ds_1)

    # Extract the mesh
    meshed_region_1 = model_1.metadata.meshed_region

There are different ways to obtain a |MeshesContainer|. You can, for example, split a |MeshedRegion| extracted
from the result file.

Here, we get a |MeshesContainer| by splitting the |MeshedRegion| by material
using the |split_mesh| operator. This operator gives a |MeshesContainer| with the |MeshedRegion| split parts
with a *'mat'* label. For more information about how to get a split mesh, see the :ref:`ref_tutorials_split_mesh`
and :ref:`ref_tutorials_extract_mesh_in_split_parts` tutorials.

.. jupyter-execute::

    # Extract the mesh in split parts
    meshes = ops.mesh.split_mesh(mesh=meshed_region_1, property="mat").eval()

Define the deforming actor
--------------------------

The geometry can be deformed by:

- A |Result| object;
- An |Operator|;
- A |Field|;
- A |FieldsContainer|.

Here, we deform the mesh using an |Operator|.

To deform the mesh we need values with a homogeneous unit dimension, a distance unit.
Thus, to deform the mesh we need the displacement results.

First, extract the displacements results |Operator| from the |Model|. For more information about extracting results
from a result file, see the :ref:`ref_tutorials_import_data` tutorials section.

.. jupyter-execute::

    # Get the displacement results Operator
    disp_results = model_1.results.displacement()

Plot the deformed mesh
----------------------

To display a deformed mesh, you can:

- :ref:`Plot the Model <ref_plot_deformed_mesh_with_model>`;
- :ref:`Plot the MeshedRegion <ref_plot_deformed_mesh_with_meshed_region>`;
- :ref:`Plot the MeshesContainer <ref_plot_deformed_mesh_with_meshes_container>`.

For all approaches, we use a scale factor so the deformed mesh fits properly on the plot.

.. jupyter-execute::

    # Define the scale factor
    scl_fct = 0.001

.. _ref_plot_deformed_mesh_with_model:

Plot the |Model|
^^^^^^^^^^^^^^^^

To plot the |Model|, you have to use the |Model.plot| method [1]_. This method plots the
bare mesh associated to the result file by default. Thus,you must also use the *'deform_by'*
argument and give the displacement results.

.. jupyter-execute::

    # Plot the deformed mesh
    model_1.plot(deform_by=disp_results,
                 scale_factor=scl_fct, )

.. _ref_plot_deformed_mesh_with_meshed_region:

Plot the |MeshedRegion|
^^^^^^^^^^^^^^^^^^^^^^^

To plot the deformed |MeshedRegion| you can use:

- The |MeshedRegion.plot| method;
- The |DpfPlotter| object.

.. tab-set::

    .. tab-item:: MeshedRegion.plot() method

        To plot the mesh with this approach, use the |MeshedRegion.plot| method [1]_ with
        the |MeshedRegion| object we defined. Additionally, you must use the *'deform_by'*
        argument and give the displacement results.

        .. jupyter-execute::

            # Plot the deformed mesh
            meshed_region_1.plot(deform_by=disp_results,
                                 scale_factor=scl_fct, )

    .. tab-item:: DpfPlotter object

        To plot the mesh with this approach, start by defining the |DpfPlotter| object [2]_.
        Then, add the |MeshedRegion| to it, using the |add_mesh| method. Additionally, you must
        use the *'deform_by'* argument and give the displacement results.

        To display the figure built by the plotter object use the |show_figure| method.

        .. jupyter-execute::

            # Declare the DpfPlotter object
            plotter_1 = dpf.plotter.DpfPlotter()

            # Add the MeshedRegion to the DpfPlotter object
            plotter_1.add_mesh(meshed_region=meshed_region_1,
                               deform_by=disp_results,
                               scale_factor=scl_fct, )

            # Display the plot
            plotter_1.show_figure()

.. _ref_plot_deformed_mesh_with_meshes_container:

Plot the |MeshesContainer|
^^^^^^^^^^^^^^^^^^^^^^^^^^

To plot the deformed |MeshesContainer| you must use the |MeshesContainer.plot| method [1]_ with
the |MeshesContainer| object we defined.Additionally, you must use the *'deform_by'*
argument and give the displacement results.

This method plots all the |MeshedRegion| stored in the |MeshesContainer| and their color code respects the
property used to split the mesh.

.. jupyter-execute::

    # Plot the deformed mesh
    meshes.plot(deform_by=disp_results,
                scale_factor=scl_fct, )

.. rubric:: Footnotes

.. [1] The default plotter settings display the mesh with edges, lighting and axis widget enabled.
Nevertheless, as we use the `PyVista <pyVista_github_>`_ library to create the plot, you can use additional
PyVista arguments (available at `pyvista.plot() <pyvista_doc_plot_method_>`_), such as:

.. jupyter-execute::

    model_1.plot(deform_by=disp_results,
                 scale_factor=scl_fct,
                 title= "Model plot",
                 text= "Model.plot()",  # Adds the given text at the bottom of the plot
                 window_size=[450, 450])
    # Notes:
    # - To save a screenshot to file, use "screenshot=figure_name.png" ( as well as "notebook=False" if on a Jupyter notebook).
    # - The "off_screen" keyword only works when "notebook=False". If "off_screen=True" the plot is not displayed when running the code.

.. [2] The |DpfPlotter| object is currently a PyVista based object.
That means that PyVista must be installed, and that it supports kwargs as
parameter (the argument must be supported by the installed PyVista version).
More information about the available arguments are available at `pyvista.plot() <pyvista_doc_plot_method_>`_.

The default |DpfPlotter| object settings displays the mesh with edges and lighting
enabled. Nevertheless, as we use the `PyVista <pyVista_github_>`_
library to create the plot, you can use additional PyVista arguments for the |DpfPlotter|
object and |add_field| method (available at `pyvista.plot() <pyvista_doc_plot_method_>`_).