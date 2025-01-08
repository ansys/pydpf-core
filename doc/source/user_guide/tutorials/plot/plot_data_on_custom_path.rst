.. _ref_plot_data_on_custom_path:

========================
Plot data on custom path
========================

.. |add_mesh| replace:: :func:`add_mesh()<ansys.dpf.core.plotter.DpfPlotter.add_mesh>`
.. |add_field| replace:: :func:`add_field()<ansys.dpf.core.plotter.DpfPlotter.add_field>`
.. |show_figure| replace:: :func:`show_figure()<ansys.dpf.core.plotter.DpfPlotter.show_figure>`
.. |Line| replace:: :class:`Line <ansys.dpf.core.geometry.Line>`
.. |Points| replace:: :class:`Points <ansys.dpf.core.geometry.Points>`
.. |Plane| replace:: :class:`Plane <ansys.dpf.core.geometry.Plane>`
.. |mapping| replace:: :class:`mapping <ansys.dpf.core.operators.mapping.on_coordinates.on_coordinates>`
.. |nodes_coordinates| replace:: :class:`nodes_coordinates<ansys.dpf.core.operators.mesh.node_coordinates.node_coordinates>`

This tutorial shows how to get a result mapped over a specific path and how to plot it.

:jupyter-download-script:`Download tutorial as Python script<plotting_data_on_specific_path>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<plotting_data_on_specific_path>`

Define the data
---------------

First, import a results file. For this tutorial, you can use the one available in the |Examples| module.
For more information about how to import your own result file in DPF, see
the :ref:`ref_tutorials_import_data` tutorials section.

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module
    from ansys.dpf import core as dpf
    # Import the examples module
    from ansys.dpf.core import examples
    # Import the operators module
    from ansys.dpf.core import operators as ops

    # Define the result file path
    result_file_path_1 = examples.find_static_rst()

The results will be mapped over a defined path of coordinates. Thus, we need the spatial support to
those coordinates: the mesh. The mesh object in DPF is a |MeshedRegion|.

You can obtain a |MeshedRegion| by creating your own from scratch or by getting it from a result file.
For more information, see the :ref:`ref_tutorials_create_a_mesh_from_scratch` and
:ref:`ref_tutorials_get_mesh_from_result_file` tutorials.

Here, we extract it from the result file.

.. jupyter-execute::

    # Create the model
    model_1 = dpf.Model(data_sources=result_file_path_1)

    # Extract the mesh
    meshed_region_1 = model_1.metadata.meshed_region

Extract the results to be plotted on the path. Here, we get the equivalent stress results.

.. jupyter-execute::

    # Get the equivalent stress results
    eq_stress = model_1.results.stress().eqv().eval()

Define the path
---------------

The path coordinates have to be in the space domain of the mesh. You can verify the
range of coordinates existing on the |MeshedRegion| by checking the nodes coordinates.

You can get the nodes coordinates with the |nodes_coordinates| operator.

.. jupyter-execute::

    # Get the nodes coordinates
    nodes_coords = ops.mesh.node_coordinates(mesh=meshed_region_1).eval()

To obtain the domain limits, get the maximal and minimal values of the nodes coordinates.

.. jupyter-execute::

    # Get the maximal nodes coordinates
    max_coords = ops.min_max.min_max(field=nodes_coords).eval(pin=1)

    # Get the minimal nodes coordinates
    min_coords = ops.min_max.min_max(field=nodes_coords).eval(pin=0)

    # Print the space domain limits
    print("Max coordinates:", max_coords.data, '\n')
    print("Min coordinates:", min_coords.data)

Create the path based on a set of coordinates. Here, define the path by choosing:

- The origin coordinates of the path;
- Number of points in the path;
- The distance between each point coordinate.

.. jupyter-execute::

    # Initial coordinates
    initial_coords = [0.024, 0.03, 0.003]

    # Number of points in the path
    n_points = 51

    # Distance between each opint coordinate
    delta = 0.001

The coordinates must be stored in a |Field|.

.. jupyter-execute::

    # Create the paths coordinates Field
    path_coords =  dpf.fields_factory.create_3d_vector_field(n_points)
    path_coords.scoping.ids = list(range(0, n_points))

Here, we make a loop to define the paths coordinates. For each iteration, we add to the |Field| a new set of
coordinates based on the predefined distance between each coordinate. The path only moves along the y-axis.

.. jupyter-execute::

    # Define the path coordinates
    for i in range(0, n_points):
        initial_coords[1] += delta
        path_coords.append(data=initial_coords, scopingid=0)

Map the results to the path
---------------------------

Map the stress data to the path using the |mapping| operator. The |mapping| operator retrieves the results
of the entities located in the given coordinates. If the given coordinates don't match with any entity coordinate,
operator interpolates the results inside elements with shape functions.


.. jupyter-execute::

    # Map the stress results to the path coordinates
    mapped_stress = ops.mapping.on_coordinates(fields_container=eq_stress,
                                               coordinates=path_coords,
                                               create_support=True,
                                               mesh=meshed_region_1
                                               ).eval()

Plot the results on the path
----------------------------

To plot the results on the path, we use the |DpfPlotter| object. For more information about
plotting data on a mesh, see the :ref:`ref_plot_data_on_a_mesh` tutorial.

First, define the |DpfPlotter| object [2]_. Next, add the |MeshedRegion|
and the |Field| using the |add_mesh| and |add_field| methods respectively.

To display the figure built by the plotter object use the |show_figure| method.

.. jupyter-execute::

    # Define the DpfPlotter object
    plotter_1 = dpf.plotter.DpfPlotter()

    # Add the MeshedRegion to the DpfPlotter object
    # We use custom style for the mesh so we can visualize the path (that is inside the mesh)
    plotter_1.add_mesh(meshed_region=meshed_region_1,
                       style="surface",show_edges=True, color="w", opacity=0.3)

    # Add the Field to the DpfPlotter object
    plotter_1.add_field(field=mapped_stress[0])

    # Display the plot
    plotter_1.show_figure()

.. rubric:: Footnotes

.. [1] The default plotter settings display the mesh with edges, lighting and axis widget enabled.
Nevertheless, as we use the `PyVista <pyVista_github_>`_ library to create the plot, you can use additional
PyVista arguments (available at `pyvista.plot() <pyvista_doc_plot_method_>`_).

.. [2] The |DpfPlotter| object is currently a PyVista based object.
That means that PyVista must be installed, and that it supports kwargs as
parameter (the argument must be supported by the installed PyVista version).
More information about the available arguments are available at `pyvista.plot() <pyvista_doc_plot_method_>`_`.

The default |DpfPlotter| object settings displays the mesh with edges and lighting
enabled. Nevertheless, as we use the `PyVista <pyVista_github_>`_
library to create the plot, you can use additional PyVista arguments for the |DpfPlotter|
object and |add_field| method (available at `pyvista.plot() <pyvista_doc_plot_method_>`_`).