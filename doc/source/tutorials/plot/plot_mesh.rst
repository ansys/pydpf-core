.. _ref_tutorials_plot_mesh:

===========
Plot a mesh
===========

.. include:: ../../../links_and_refs.rst

.. |Model.plot| replace:: :py:meth:`Model.plot() <ansys.dpf.core.model.Model.plot>`
.. |MeshedRegion.plot| replace:: :py:meth:`MeshedRegion.plot() <ansys.dpf.core.meshed_region.MeshedRegion.plot>`
.. |MeshesContainer.plot| replace:: :py:meth:`MeshesContainer.plot() <ansys.dpf.core.meshes_container.MeshesContainer.plot>`
.. |add_mesh| replace:: :py:meth:`add_mesh() <ansys.dpf.core.plotter.DpfPlotter.add_mesh>`
.. |show_figure| replace:: :py:meth:`show_figure() <ansys.dpf.core.plotter.DpfPlotter.show_figure>`
.. |split_mesh| replace:: :py:class:`split_mesh <ansys.dpf.core.operators.mesh.split_mesh.split_mesh>`

This tutorial shows different commands for plotting a mesh without data.

A mesh is represented in DPF by a |MeshedRegion| object.
You can store multiple |MeshedRegion| in a DPF collection called |MeshesContainer|.

You can obtain a |MeshedRegion| by creating your own from scratch or by getting it from a result file.
For more information, see the :ref:`ref_tutorials_create_a_mesh_from_scratch` and
:ref:`ref_tutorials_get_mesh_from_result_file` tutorials.

PyDPF-Core has a variety of plotting methods for generating 3D plots with Python.
These methods use VTK and leverage the `PyVista <https://github.com/pyvista/pyvista>`_ library.

:jupyter-download-script:`Download tutorial as Python script<plot_mesh>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<plot_mesh>`

Load data to plot
-----------------

For this tutorial, we use mesh information from a case available in the |Examples| module.
For more information see the :ref:`ref_tutorials_get_mesh_from_result_file` tutorial.

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module
    import ansys.dpf.core as dpf
    # Import the examples module
    from ansys.dpf.core import examples
    # Import the operators module
    from ansys.dpf.core import operators as ops

    # Download and get the path to an example result file
    result_file_path_1 = examples.download_piston_rod()

    # Create a model from the result file
    model_1 = dpf.Model(data_sources=result_file_path_1)

Plot a model
------------

You can directly plot the overall mesh loaded by the model with |Model.plot| [1]_.

.. jupyter-execute::

    # Plot the mesh
    model_1.plot()

Plot a single mesh
------------------

Get the mesh
^^^^^^^^^^^^

Here we simply get the |MeshedRegion| object of the model, but any other |MeshedRegion| works.

.. jupyter-execute::

    # Extract the mesh
    meshed_region_1 = model_1.metadata.meshed_region

Plot the mesh
^^^^^^^^^^^^^

To plot the |MeshedRegion| you can use:

- The |MeshedRegion.plot| method;
- The |DpfPlotter| object.

.. tab-set::

    .. tab-item:: MeshedRegion.plot() method

        Use the |MeshedRegion.plot| method [1]_ of the |MeshedRegion| object we defined.

        .. jupyter-execute::

            # Plot the mesh object
            meshed_region_1.plot()

    .. tab-item:: DpfPlotter object

        To plot the mesh with this approach, first create an instance of |DpfPlotter| [2]_.
        Then, add the |MeshedRegion| to the scene using the |add_mesh| method.

        To render and show the figure based on the current state of the plotter object, use the |show_figure| method.

        .. jupyter-execute::

            # Create a DpfPlotter instance
            plotter_1 = dpf.plotter.DpfPlotter()

            # Add the mesh to the scene
            plotter_1.add_mesh(meshed_region=meshed_region_1)

            # Display the scene
            plotter_1.show_figure()

You can also plot data contours on a mesh. For more information, see :ref:`ref_tutorials_plot_contour`

Plot several meshes
-------------------

Build a collection of meshes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are different ways to obtain a |MeshesContainer|.
You can for example split a |MeshedRegion| using operators.

Here, we use the |split_mesh| operator to split the mesh based on the material of each element.
This operator returns a |MeshesContainer| with meshes labeled according to the criterion for the split.
In our case, each mesh has a *'mat'* label.
For more information about how to get a split mesh, see the :ref:`ref_tutorials_split_mesh`
and :ref:`ref_tutorials_extract_mesh_in_split_parts` tutorials.

.. jupyter-execute::

    # Split the mesh based on material property
    meshes = ops.mesh.split_mesh(mesh=meshed_region_1, property="mat").eval()

    # Show the result
    print(meshes)

Plot the meshes
^^^^^^^^^^^^^^^

Use the |MeshesContainer.plot| method [1]_ of the |MeshesContainer| object we defined.

This method plots all the |MeshedRegion| objects stored in the |MeshesContainer|
and colors them based on the property used to split the mesh.

.. jupyter-execute::

    # Plot the collection of meshes
    meshes.plot()

You can also plot data on a collection of meshes.
For more information, see :ref:`ref_tutorials_plot_contour`

.. rubric:: Footnotes

.. [1] The |DpfPlotter| displays the mesh with edges, lighting and axis widget enabled by default.
    You can pass additional PyVista arguments to all plotting methods to change the default behavior
    (see options for `pyvista.plot() <https://docs.pyvista.org/api/plotting/_autosummary/pyvista.plot.html#pyvista.plot>`_), such as:

    .. jupyter-execute::

        model_1.plot(title="Mesh",
                     text="this is a mesh",  # Adds the given text at the bottom of the plot
                     off_screen=True,
                     screenshot="mesh_plot_1.png",  # Save a screenshot to file with the given name
                     window_size=[450,350])
        # Notes:
        # - To save a screenshot to file, use "screenshot=figure_name.png" ( as well as "notebook=False" if on a Jupyter notebook).
        # - The "off_screen" keyword only works when "notebook=False". If "off_screen=True" the plot is not displayed when running the code.

.. [2] The |DpfPlotter| is currently based on PyVista.
    That means that PyVista must be installed.
    The DPF plotter also passes additional parameters to the PyVista plotter
    (arguments supported by the version of PyVista installed).
    More information about available additional arguments is available at `pyvista.plot() <https://docs.pyvista.org/api/plotting/_autosummary/pyvista.plot.html#pyvista.plot>`_.
