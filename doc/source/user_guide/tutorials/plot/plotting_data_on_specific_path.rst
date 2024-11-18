.. _ref_plotting_data_on_specific_path:

================================
Plotting data on a specific path
================================

.. |DpfPlotter| replace:: :class:`DpfPlotter<ansys.dpf.core.plotter.DpfPlotter>`
.. |add_mesh| replace:: :func:`add_mesh()<ansys.dpf.core.plotter.DpfPlotter.add_mesh>`
.. |add_field| replace:: :func:`add_field()<ansys.dpf.core.plotter.DpfPlotter.add_field>`
.. |show_figure| replace:: :func:`show_figure()<ansys.dpf.core.plotter.DpfPlotter.show_figure>`
.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |Line| replace:: :class:`Line <ansys.dpf.core.geometry.Line>`
.. |Points| replace:: :class:`Points <ansys.dpf.core.geometry.Points>`
.. |Plane| replace:: :class:`Plane <ansys.dpf.core.geometry.Plane>`
.. |mapping| replace:: :class:`mapping <ansys.dpf.core.operators.mapping.on_coordinates.on_coordinates>`

This tutorial shows how to get a result mapped over a specific path and how to plot it.

Define the data
---------------

We will download a simple simulation result file available in our `Examples` package:

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    # Define the result file
    result_file = examples.find_static_rst()

The results will be mapped over a defined path of coordinates. So, start by creating
a |Model| with the result file and extract the |MeshedRegion| from it:

.. code-block:: python

    # Create the model
    my_model = dpf.Model(data_sources=result_file)
    my_meshed_region = my_model.metadata.meshed_region

Define the path
---------------

The path coordinates have to be in the space domain of the mesh. You can verify the
range of coordinates values by checking the nodes coordinates.

Get the nodes coordinates with the mesh operator
:class:`nodes_coordinates<ansys.dpf.core.operators.mesh.node_coordinates.node_coordinates>`:

.. code-block:: python

    # Get the mesh nodes coordinates
    nodes_coords = ops.mesh.node_coordinates(mesh=my_meshed_region).eval()

Get the maximum values of the coordinates, so you know the space domain limits.

.. code-block:: python

    # Get the maximum and minimum values of the mesh nodes coordinates
    max_coords = ops.min_max.min_max(field=nodes_coords).eval(pin=1)
    min_coords = ops.min_max.min_max(field=nodes_coords).eval(pin=0)
    # Print the space domain limits
    print("Max coordinates:", max_coords.data, '\n')
    print("Min coordinates:",min_coords.data)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    result_file = examples.find_static_rst()
    my_model = dpf.Model(data_sources=result_file)
    my_meshed_region = my_model.metadata.meshed_region
    nodes_coords = ops.mesh.node_coordinates(mesh=my_meshed_region).eval()
    max_coords = ops.min_max.min_max(field=nodes_coords).eval(pin=1)
    min_coords = ops.min_max.min_max(field=nodes_coords).eval(pin=0)
    print("Max coordinates:", max_coords.data, '\n')
    print("Min coordinates:",min_coords.data)


Create the path based on a set of coordinates. Here we choose the paths origin coordinates,
number of points in the path and the distance between each coordinate.

.. code-block:: python

    # Initial coordinates
    initial_coords = [0.024, 0.03, 0.003]
    # Number of points in the path
    n_points = 51
    # Distance between each coordinate
    delta = 0.001

    # Create the paths coordinates field
    path_coords =  dpf.fields_factory.create_3d_vector_field(n_points)
    path_coords.scoping.ids = list(range(0, n_points))

Make a loop to define the paths coordinates field. Here we make a path that only moves along the y-axis.

.. code-block:: python

    # For each iteration we add a new set of coordinates based on the predefined distance between each coordinate
    for i in range(0, n_points):
        initial_coords[1] += delta
        path_coords.append(data=initial_coords, scopingid=0)

Extract the result
------------------

Extract the result from the model. Here we get the equivalent stress result

.. code-block:: python

    # Get the stress result
    my_stress = my_model.results.stress().eqv().eval()

Map the result to the path
--------------------------

Compute the mapped data using the |mapping| operator. The stress results are defined in a ``ElementalNodal`` location.
So, each entity has a coordinate in the mesh and a correspondent stress data.

The |mapping| operator retrieves the results of the entities located in the given coordinates.
If the given coordinates don't match with any entity coordinate, the operator interpolates the results inside
elements with shape functions.

.. code-block:: python

    # Map the path coordinates with the stress results
    mapped_stress = ops.mapping.on_coordinates(fields_container=my_stress,
                                               coordinates=path_coords,
                                               create_support=True,
                                               mesh=my_meshed_region
                                               ).eval()

Plot the result on the path
---------------------------

Create the plotter and add fields and meshes. For more information about
plotting data on a mesh check the tutorial: :ref:`ref_plotting_data_on_the_mesh`

First, define the |DpfPlotter| object [2]_, then add |MeshedRegion|
to it using the |add_mesh| method and add the field using the |add_field| method.

To display the figure built by the plotter object use the |show_figure|  method.

.. code-block:: python

    # Declare the DpfPlotter object
    my_plotter = dpf.plotter.DpfPlotter()
    # Add the MeshedRegion to the DpfPlotter object
    # We use custom style for the mesh so we can visualise the path (that is inside the mesh)
    my_plotter.add_mesh(meshed_region=my_meshed_region,style="surface", show_edges=True, color="w", opacity=0.3)
    # Add the Field to the DpfPlotter object
    my_plotter.add_field(field=mapped_stress[0])
    # Display the plot
    my_plotter.show_figure()

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    initial_coords = [0.024, 0.03, 0.003]
    n_points = 51
    delta = 0.001
    path_coords =  dpf.fields_factory.create_3d_vector_field(n_points)
    path_coords.scoping.ids = list(range(0, n_points))
    for i in range(0, n_points):
        initial_coords[1] += delta
        path_coords.append(data=initial_coords, scopingid=0)
    my_stress = my_model.results.stress().eqv().eval()
    mapped_stress = ops.mapping.on_coordinates(fields_container=my_stress,
                                               coordinates=path_coords,
                                               create_support=True,
                                               mesh=my_meshed_region
                                               ).eval()
    my_plotter = dpf.plotter.DpfPlotter()
    my_plotter.add_mesh(meshed_region=my_meshed_region,style="surface", show_edges=True, color="w", opacity=0.3)
    my_plotter.add_field(field=mapped_stress[0])
    my_plotter.show_figure()

.. rubric:: Footnotes

.. [1] The default plotter settings display the mesh with edges, lighting and axis widget enabled.
Nevertheless, as we use the `PyVista <https://github.com/pyvista/pyvista>`_ library to create
the plot you can use additional PyVista arguments (available at: :func:`pyvista.plot`).

.. [2] Here we use the |DpfPlotter| object, that is currently a PyVista based object.
That means that PyVista must be installed, and that it supports kwargs as
parameter (the argument must be supported by the installed PyVista version).

The default |DpfPlotter| object settings display the mesh with edges and lighting
enabled. Nevertheless, as we use the `PyVista <https://github.com/pyvista/pyvista>`_
library to create the plot you can use additional PyVista arguments for the |DpfPlotter|
object and |add_field| method (available at: :func:`pyvista.plot`).