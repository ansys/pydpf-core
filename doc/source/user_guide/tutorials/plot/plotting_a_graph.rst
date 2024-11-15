.. _ref_plotting_a_graph:

========================
Plotting data on a graph
========================

.. |DpfPlotter| replace:: :class:`DpfPlotter<ansys.dpf.core.plotter.DpfPlotter>`
.. |Line| replace:: :class:`Line <ansys.dpf.core.geometry.Line>`
.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |mapping| replace:: :class:`mapping <ansys.dpf.core.operators.mapping.on_coordinates.on_coordinates>`

This part shows how to get a result plotted on a graph.

The current |DpfPlotter| module don't have method to plotting graphs. Thus, you need to import the
`matplotlib <https://github.com/matplotlib/matplotlib>`_ library to plot a graph with PyDPF-Core.

There is a large range of data types you can represent on the graph coordinates. Here we plot:

- `Results data vs. space position`_ graph
- `Results data vs. time`_ graph

Results data vs. space position
-------------------------------

We will plot the displacement results on a |Line|. To understand how this object can
be defined check the :ref:`ref_plotting_data_on_specific_placements` tutorial.

Define the data
^^^^^^^^^^^^^^^

We will download a simple simulation result file available in our `Examples` package:

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples files, the operators subpackage, the geometry module and the matplotlib
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    from ansys.dpf.core import geometry as geo
    import matplotlib.pyplot as plt
    # Define the result file
    result_file = examples.find_static_rst()

The results will be mapped over a defined path of coordinates. So, start by creating
a |Model| with the result file and extract the |MeshedRegion| from it:

.. code-block:: python

    # Create the model
    my_model = dpf.Model(data_sources=result_file)
    my_meshed_region = my_model.metadata.meshed_region

We choose to plot the displacement results field. Extract the displacements results from the model:

.. code-block:: python

    # Get the displacement results
    my_disp = my_model.results.displacement.eval()

Create the line
^^^^^^^^^^^^^^^

Create a |Line| passing through the mesh diagonal.

.. code-block:: python

    # Create the Line object
    my_line = geo.Line(coordinates=[[0.0, 0.06, 0.0], [0.03, 0.03, 0.03]],
                       n_points=50
                       )

Map displacement field to the line
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute the mapped displacement data using the |mapping| operator.

.. code-block:: python

    # Map the line coordinates with the displacement results and get the field
    mapped_disp_line = ops.mapping.on_coordinates(fields_container=my_disp,
                                                  coordinates=my_line.mesh.nodes.coordinates_field,
                                                  create_support=True,
                                                  mesh=my_meshed_region
                                                   ).eval()[0]

Plot a graph of the displacement results along the specified line
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plot a graph of the displacement field along the specified |Line| length using the matplotlib library.

To get the |Line| length you can use the |Line| property :func:`path<ansys.dpf.core.geometry.Line.path>`.
It gives the 1D line coordinates, by the number of points the line was discretized.

.. code-block:: python

    # Define the norm of the displacement field
    norm_disp = ops.math.norm(field=mapped_disp_line).eval()
    # Define the line points on the its length
    line_length_points = my_line.path
    # Plot the graph
    plt.plot(line_length_points, norm_disp)
    # Graph formating
    plt.xlabel("Line length");  plt.ylabel("Displacement norm field"); plt.title("Displacement evolution on the line")
    plt.show()

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    from ansys.dpf.core import geometry as geo
    import matplotlib.pyplot as plt
    result_file = examples.find_static_rst()
    my_model = dpf.Model(data_sources=result_file)
    my_meshed_region = my_model.metadata.meshed_region
    my_disp = my_model.results.displacement.eval()
    my_line = geo.Line(coordinates=[[0.0, 0.06, 0.0], [0.03, 0.03, 0.03]],
                       n_points=50
                       )
    mapped_disp_line = ops.mapping.on_coordinates(fields_container=my_disp,
                                                  coordinates=my_line.mesh.nodes.coordinates_field,
                                                  create_support=True,
                                                  mesh=my_meshed_region
                                                   ).eval()[0]
    norm_disp = ops.math.norm(field=mapped_disp_line).eval()
    line_length_points = my_line.path
    plt.plot(line_length_points, norm_disp.data)
    plt.xlabel("Line length");  plt.ylabel("Displacement norm field"); plt.title("Displacement evolution on the line")
    plt.show()

Results data vs. time
---------------------

We will plot the displacement results over time for a transient analysis. To understand more about using PyDPF-Core
with a transient analysis check the :ref:`static_transient_examples` examples.

Define the data
^^^^^^^^^^^^^^^

Download the transient result example. This example is not included in DPF-Core
by default to speed up the installation. Downloading this example should take only a few seconds.

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples files, the operators subpackage and the matplotlib
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    import matplotlib.pyplot as plt
    # Define the result file
    result_file = examples.download_transient_result()

The results will be mapped over a defined path of coordinates. So, start by creating
a |Model| with the result file and extract the |MeshedRegion| from it:

.. code-block:: python

    # Create the model
    my_model = dpf.Model(data_sources=result_file)
    my_meshed_region = my_model.metadata.meshed_region

We choose to plot the maximum and minimum displacement results over time.
Extract the displacements results from the model for all the time frequencies:

.. code-block:: python

    # Get the displacement results
    my_disp = my_model.results.displacement.on_all_time_freqs.eval()

Define the minimum and maximum displacements for all results:

.. code-block:: python

    # Define the min_max operator with the normed displacement
    min_max_op = ops.min_max.min_max_fc(fields_container=ops.math.norm_fc(my_disp))
    # Get the max and min displacements
    max_disp = min_max_op.eval(pin=1)
    min_disp = min_max_op.eval(pin=0)

Plot a graph of the minimum and maximum displacements over time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plot a graph of the minimum and maximum displacements over time using the matplotlib library.

.. code-block:: python

    # Define the time frequencies from the model
    time_data = my_model.metadata.time_freq_support.time_frequencies.data
    # Plot the graph
    plt.plot(time_data, max_disp.data, "r", label="Max")
    plt.plot(time_data, min_disp.data, "b", label="Min")
    # Graph formating
    plt.xlabel("Time (s)"); plt.ylabel("Displacement (m)"); plt.legend(); plt.show()

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    import matplotlib.pyplot as plt
    result_file = examples.download_transient_result()
    my_model = dpf.Model(data_sources=result_file)
    my_meshed_region = my_model.metadata.meshed_region
    my_disp = my_model.results.displacement.on_all_time_freqs.eval()
    min_max_op = ops.min_max.min_max_fc(fields_container=ops.math.norm_fc(my_disp))
    max_disp = min_max_op.eval(pin=1)
    min_disp = min_max_op.eval(pin=0)
    time_data = my_model.metadata.time_freq_support.time_frequencies.data
    plt.plot(time_data, max_disp.data, "r", label="Max")
    plt.plot(time_data, min_disp.data, "b", label="Min")
    plt.xlabel("Time (s)"); plt.ylabel("Displacement (m)"); plt.legend(); plt.show()