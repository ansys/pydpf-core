.. _ref_plot_a_graph:

====================
Plot data on a graph
====================

.. |Line| replace:: :class:`Line <ansys.dpf.core.geometry.Line>`
.. |mapping| replace:: :class:`mapping <ansys.dpf.core.operators.mapping.on_coordinates.on_coordinates>`
.. |Line.path| replace:: :func:`Line.path<ansys.dpf.core.geometry.Line.path>`
.. |min_max_fc| replace:: :class:`min_max_fc <ansys.dpf.core.operators.min_max.min_max_fc.min_max_fc>`

This tutorial explains how to plot a graph with data in DPF.

The current |DpfPlotter| module don't have method to plotting graphs. Thus, you need to import the
`matplotlib <matplotlib_github_>`_ library to plot a graph with PyDPF-Core.

There is a large range of graphs you can plot. Here, we plot:

- :ref:`Results data vs. space position graph <ref_graph_result_space>`
- :ref:`Results data vs. time graph <ref_graph_result_time>`

.. _ref_graph_result_space:

Results data vs. space position
-------------------------------

In this tutorial, we plot the norm of the displacement results on a |Line|. For more information about how
this object can be defined, see the :ref:`ref_plot_data_on_custom_geometry` tutorial.

Define the results data
^^^^^^^^^^^^^^^^^^^^^^^

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
    # Import the geometry module
    from ansys.dpf.core import geometry as geo

    # Import the ``matplotlib.pyplot`` module
    import matplotlib.pyplot as plt

    # Define the result file path
    result_file_path_1 = examples.find_static_rst()

The results will be mapped over a defined set of coordinates. Thus, we need the spatial support to
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

Extract the results to be plotted on the graph. In this tutorial, we plot the norm of the
displacement results over time.

.. jupyter-execute::

    # Get the displacement results
    disp_results_1 = model_1.results.displacement.eval()

Define the line
^^^^^^^^^^^^^^^

Create a |Line| passing through the mesh diagonal.

.. jupyter-execute::

    # Create the Line object
    line_1 = geo.Line(coordinates=[[0.0, 0.06, 0.0], [0.03, 0.03, 0.03]],
                       n_points=50
                       )

Map the results to the line
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Map the displacement results to the |Line| using the |mapping| operator. This operator
retrieves the results of the entities located in the given coordinates. If the given coordinates don't
match with any entity coordinate, the operator interpolates the results inside elements with shape functions.

The displacement results are defined in a *`nodal`* location. Thus, each node has a coordinate in the
mesh and a corresponding displacement data.

The |mapping| operator takes the coordinates stored in a |Field|. Thus, we must create a |Field| with the
|Line| coordinates.

.. jupyter-execute::

    # Get the coordinates field
    line_coords_field = line_1.mesh.nodes.coordinates_field

    # Map the line coordinates with the displacement results
    mapped_disp_line = ops.mapping.on_coordinates(fields_container=disp_results_1,
                                                  coordinates=line_coords_field,
                                                  create_support=True,
                                                  mesh=meshed_region_1
                                                   ).eval()[0]

Plot the graph
^^^^^^^^^^^^^^

Plot a graph of the norm of the displacement results along the |Line| length using the
`matplotlib <matplotlib_github_>`_ library.

To get the |Line| length you can use the |Line.path| method. It gives the 1D line coordinates, based on
the points where the line was discretized.

.. jupyter-execute::

    # Define the norm of the displacement results
    norm_disp = ops.math.norm(field=mapped_disp_line).eval()

    # Define the point coordinates on the line length
    line_length_points = line_1.path

    # Define the plot figure
    plt.plot(line_length_points, norm_disp.data)

    # Graph formating
    plt.xlabel("Line length");  plt.ylabel("Displacement norm field"); plt.title("Displacement evolution on the line")

    # Display the graph
    plt.show()

.. _ref_graph_result_time:

Results data vs. time
---------------------

In this tutorial, we plot the displacement results over time for a transient analysis.
For more information about using PyDPF-Core with a transient analysis, see the :ref:`static_transient_examples` examples.

Define the results data
^^^^^^^^^^^^^^^^^^^^^^^

First, import a transient results file. For this tutorial, you can use the one available in the |Examples| module.
For more information about how to import your own result file in DPF, see
the :ref:`ref_tutorials_import_data` tutorials section.

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module
    from ansys.dpf import core as dpf
    # Import the examples module
    from ansys.dpf.core import examples
    # Import the operators module
    from ansys.dpf.core import operators as ops

    # Import the ``matplotlib.pyplot`` module
    import matplotlib.pyplot as plt

    # Define the result file path
    result_file_path_2 = examples.download_transient_result()

The results will be mapped over a defined path of coordinates. Thus, we need the spatial support to
those coordinates: the mesh. The mesh object in DPF is a |MeshedRegion|.

You can obtain a |MeshedRegion| by creating your own from scratch or by getting it from a result file.
For more information, see the :ref:`ref_tutorials_create_a_mesh_from_scratch` and
:ref:`ref_tutorials_get_mesh_from_result_file` tutorials.

Here, we extract it from the result file.

.. jupyter-execute::

    # Create the model
    model_2 = dpf.Model(data_sources=result_file_path_2)

    # Extract the mesh
    meshed_region_2 = model_2.metadata.meshed_region

Extract the results to be plotted on the graph. Here, we plot the maximum and minimum
displacement results over time.

First extract the displacement results for all the time frequencies.

.. jupyter-execute::

    # Get the displacement results
    disp_results_2 = model_2.results.displacement.on_all_time_freqs.eval()

Next, define the minimal and maximal displacements for each time step by using the |min_max_fc|
operator.

.. jupyter-execute::

    # Define the min_max operator and give the normed displacement results
    min_max_op = ops.min_max.min_max_fc(fields_container=ops.math.norm_fc(disp_results_2))

    # Get the max displacement results
    max_disp = min_max_op.eval(pin=1)

    # Get the min displacement results
    min_disp = min_max_op.eval(pin=0)

Define the time data
^^^^^^^^^^^^^^^^^^^^

The results time steps in DPF are given by the |TimeFreqSupport| object. You can extract it
from the displacement results |Field|.

.. jupyter-execute::

    # Define the time steps
    time_steps_1 = disp_results_2.time_freq_support.time_frequencies

    # Print the time frequencies
    print(time_steps_1)

The time steps are given in a |Field|. To plot the graph you need to extract the
|Field| data.

.. jupyter-execute::

    # Get the time steps data
    time_data = time_steps_1.data


Plot the graph
^^^^^^^^^^^^^^

Plot a graph of the minimal and maximal displacements over time using the
`matplotlib <matplotlib_github_>`_ library.

.. jupyter-execute::

    # Define the plot figure
    plt.plot(time_data, max_disp.data, "r", label="Max")
    plt.plot(time_data, min_disp.data, "b", label="Min")

    # Graph formating
    plt.xlabel("Time (s)"); plt.ylabel("Displacement (m)"); plt.legend();

    # Display the graph
    plt.show()