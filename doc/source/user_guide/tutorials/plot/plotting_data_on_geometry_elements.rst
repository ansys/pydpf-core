.. _ref_plotting_data_on_geometry_elements:

==============================
Plot data on geometry elements
==============================

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

This tutorials shows how to get a result mapped over different geometric objects:

- Points_
- Line_
- Plane_

Define the data
---------------

We will download a simple simulation result file available in our `Examples` package:

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples files, the operators subpackage and the geometry module
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    from ansys.dpf.core import geometry as geo
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

We use the the plot method [1]_ to display the geometry elements with the mesh. To a better
visualisation we will define a camera position. It can be given as an argument when using the
plot method [1]_:

.. code-block:: python

    # Define the camera position
    camera_position = [
    (0.07635352356975698, 0.1200500294271993, 0.041072502929096165),
    (0.015, 0.045, 0.015),
    (-0.16771051558419411, -0.1983722658245161, 0.9656715938216944),
    ]

Points
------

Create points
^^^^^^^^^^^^^

Create |Points| by defining their coordinates. They have to be in the space
domain of the mesh. You can verify the range of coordinates values by checking
the nodes coordinates.

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
    from ansys.dpf.core import geometry as geo
    result_file = examples.find_static_rst()
    my_model = dpf.Model(data_sources=result_file)
    my_meshed_region = my_model.metadata.meshed_region
    my_disp = my_model.results.displacement
    camera_position = [
    (0.07635352356975698, 0.1200500294271993, 0.041072502929096165),
    (0.015, 0.045, 0.015),
    (-0.16771051558419411, -0.1983722658245161, 0.9656715938216944),
    ]
    nodes_coords = ops.mesh.node_coordinates(mesh=my_meshed_region).eval()
    max_coords = ops.min_max.min_max(field=nodes_coords).eval(pin=1)
    min_coords = ops.min_max.min_max(field=nodes_coords).eval(pin=0)
    print("Max coordinates:", max_coords.data, '\n')
    print("Min coordinates:",min_coords.data)

Now define the |Points| coordinates that respects those space limits.

With the maximum and minimum coordinates we can can deduce the nodes at the corners of the mesh.

The coordinates are define at the global Cartesian coordinates system by default. Thus, combining
the max and min coordinates gives us the points that will be in the corner of the mesh. We can also
place one point in the middle of the mesh by calculating the middle distance between the coordinates.

You can do it by hand or by calculating this combinations :

.. code-block:: python

    # Define the coordinates of the  middle point
    # print(min_coords.data_as_list)
    distance_minmax_coords = ops.math.minus(fieldA=max_coords.data_as_list, fieldB=min_coords.data_as_list).eval()
    middle = ops.math.scale(field=distance_minmax_coords, ponderation=0.5).eval()
    middle_coords = ops.math.add(fieldA=min_coords.data_as_list,fieldB=middle.data_as_list).eval()
    # Define the points
    my_points = geo.Points(coordinates=[
                                      [0.0, 0.03, 0.0],
                                      [0.0, 0.06, 0.0],
                                      [0.03, 0.06, 0.0],
                                      [0.03, 0.03, 0.0],
                                      [0.0, 0.03, 0.03],
                                      [0.0, 0.06, 0.03],
                                      [0.03, 0.06, 0.03],
                                      [0.03, 0.03, 0.03],
                                      middle_coords.data_as_list
                                    ]
                        )

Check the points on the mesh with a plot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can plot the |Points| together with the mesh:

.. code-block:: python

    # Display the mesh and the points
    my_points.plot(mesh=my_meshed_region, cpos=camera_position)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    distance_minmax_coords = ops.math.minus(fieldA=max_coords.data_as_list, fieldB=min_coords.data_as_list).eval()
    middle = ops.math.scale(field=distance_minmax_coords, ponderation=0.5).eval()
    middle_coords = ops.math.add(fieldA=min_coords.data_as_list,fieldB=middle.data_as_list).eval()
    my_points = geo.Points(coordinates=[
                                      [0.0, 0.03, 0.0],
                                      [0.0, 0.06, 0.0],
                                      [0.03, 0.06, 0.0],
                                      [0.03, 0.03, 0.0],
                                      [0.0, 0.03, 0.03],
                                      [0.0, 0.06, 0.03],
                                      [0.03, 0.06, 0.03],
                                      [0.03, 0.03, 0.03],
                                      middle_coords.data_as_list
                                    ]
                        )
    my_points.plot(mesh=my_meshed_region, cpos=camera_position)

Map displacement field to the points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute the mapped data using the |mapping| operator. The displacement results are defined in a ``Nodal`` location.
So, each node has a coordinate in the mesh and a correspondent displacement data.

The |mapping| operator retrieves the results of the entities located in the given coordinates.
If the given coordinates don't match with any entity coordinate, the operator interpolates the results inside
elements with shape functions.

.. code-block:: python

    # Map the points coordinates with the displacement results and get the field
    mapped_disp_points = ops.mapping.on_coordinates(fields_container=my_disp,
                                                    coordinates=dpf.fields_factory.field_from_array(arr=my_points.coordinates.data),
                                                    create_support=True,
                                                    mesh=my_meshed_region
                                                    ).eval()[0]

Plot displacement field on the points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create the plotter and add fields and meshes. For more information about
plotting data on a mesh check the tutorial: :ref:`ref_plotting_data_on_the_mesh`

First, define the |DpfPlotter| object [2]_, then add |MeshedRegion|
to it using the |add_mesh| method and add the field using the |add_field| method.

To display the figure built by the plotter object use the |show_figure| method.

.. code-block:: python

    # Declare the DpfPlotter object
    my_plotter = dpf.plotter.DpfPlotter()
    # Add the MeshedRegion to the DpfPlotter object
    # We use custom style for the mesh so we can visualise the points
    my_plotter.add_mesh(meshed_region=my_meshed_region,style="surface", show_edges=True, color="w", opacity=0.3)
    # Add the Field to the DpfPlotter object
    my_plotter.add_field(field=mapped_disp_points, point_size=20.0, render_points_as_spheres=True)
    # Display the plot
    my_plotter.show_figure(show_axes=True, cpos=camera_position)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    mapped_disp_points = ops.mapping.on_coordinates(fields_container=my_disp,
                                                    coordinates=dpf.fields_factory.field_from_array(arr=my_points.coordinates.data),
                                                    create_support=True,
                                                    mesh=my_meshed_region
                                                    ).eval()[0]
    my_plotter = dpf.plotter.DpfPlotter()
    my_plotter.add_mesh(meshed_region=my_meshed_region,style="surface", show_edges=True, color="w", opacity=0.3)
    my_plotter.add_field(field=mapped_disp_points,point_size=20.0, render_points_as_spheres=True)
    my_plotter.show_figure(show_axes=True, cpos=camera_position)

Line
----

Create the line
^^^^^^^^^^^^^^^

Create a |Line| passing through the mesh diagonal. To create a |Line|
you need pass as arguments: the coordinates of the starting and ending points
and the number of points where the |Line| object will be discretized.

Check the `Create points`_ section to understand how we defined the points coordinates.

.. code-block:: python

    # Create the Line object
    my_line = geo.Line(coordinates=[[0.0, 0.06, 0.0], [0.03, 0.03, 0.03]],
                       n_points=50
                       )

Check the line on the mesh with a plot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can plot the |Line| together with the mesh:

.. code-block:: python

    # Display the mesh and the line
    my_line.plot(mesh=my_meshed_region, cpos=camera_position)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_line = geo.Line(coordinates=[[0.0, 0.06, 0.0], [0.03, 0.03, 0.03]],
                       n_points=50
                       )
    my_line.plot(mesh=my_meshed_region, cpos=camera_position)

Map displacement field to the line
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute the mapped data using the |mapping| operator. The displacement results are defined in a ``Nodal`` location.
So, each node has a coordinate in the mesh and a correspondent displacement data.

The |mapping| operator retrieves the results of the entities located in the given coordinates.
If the given coordinates don't match with any entity coordinate, the operator interpolates the results inside
elements with shape functions.

.. code-block:: python

    # Map the line coordinates with the displacement results and get the field
    mapped_disp_line = ops.mapping.on_coordinates(fields_container=my_disp,
                                                  coordinates=my_line.mesh.nodes.coordinates_field,
                                                  create_support=True,
                                                  mesh=my_meshed_region
                                                   ).eval()[0]

Plot displacement field on the line
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plot displacement field on the |Line| and display mesh in background.
Create the plotter and add fields and meshes. For more information about
plotting data on a mesh check the tutorial: :ref:`ref_plotting_data_on_the_mesh`

First, define the |DpfPlotter| object [2]_, then add |MeshedRegion|
to it using the |add_mesh| method and add the field using the |add_field| method.

To display the figure built by the plotter object use the |show_figure| method.

.. code-block:: python

    # Declare the DpfPlotter object
    my_plotter = dpf.plotter.DpfPlotter()
    # Add the MeshedRegion to the DpfPlotter object
    # We use custom style for the mesh so we can visualise the points
    my_plotter.add_mesh(meshed_region=my_meshed_region,style="surface", show_edges=True, color="w", opacity=0.3)
    # Add the Field to the DpfPlotter object
    my_plotter.add_field(field=mapped_disp_line)
    # Display the plot
    my_plotter.show_figure(show_axes=True, cpos=camera_position)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    mapped_disp_line = ops.mapping.on_coordinates(fields_container=my_disp,
                                                  coordinates=my_line.mesh.nodes.coordinates_field,
                                                  create_support=True,
                                                  mesh=my_meshed_region
                                                   ).eval()[0]
    my_plotter = dpf.plotter.DpfPlotter()
    my_plotter.add_mesh(meshed_region=my_meshed_region,style="surface", show_edges=True, color="w", opacity=0.3)
    my_plotter.add_field(field=mapped_disp_line,meshed_region=my_line.mesh)
    my_plotter.show_figure(show_axes=True, cpos=camera_position)

Plane
-----

Create the plane
^^^^^^^^^^^^^^^^

Create a vertical |Plane| passing through the mesh mid point. To create a |Plane|
you need pass as arguments: the coordinates of the center point, the vector of the normal direction to the plane,
and the width (x direction), height (y direction) and the number of cells(x and y direction) where the |Plane|
object will be discretized.

Check the `Create points`_ section to understand how we defined the mesh space coordinates .

.. code-block:: python

    # Create the Plane object
    my_plane = geo.Plane(center=middle_coords.data_as_list,
                         normal=[1, 1, 0],
                         width=0.03,
                         height=0.03,
                         n_cells_x=10,
                         n_cells_y=10,
                         )

Check the plane on the mesh with a plot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can plot the |Plane| together with the mesh:

.. code-block:: python

    # Display the mesh and the plane
    my_plane.plot(mesh=my_meshed_region, cpos=camera_position)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_plane = geo.Plane(center=middle_coords.data_as_list,
                         normal=[1, 1, 0],
                         width=0.03,
                         height=0.03,
                         n_cells_x=10,
                         n_cells_y=10,
                         )
    my_plane.plot(mesh=my_meshed_region, cpos=camera_position)

Map displacement field to the plane
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute the mapped data using the |mapping| operator. The displacement results are defined in a ``Nodal`` location.
So, each node has a coordinate in the mesh and a correspondent displacement data.

The |mapping| operator retrieves the results of the entities located in the given coordinates.
If the given coordinates don't match with any entity coordinate, the operator interpolates the results inside
elements with shape functions.

.. code-block:: python

    # Map the line coordinates with the displacement results and get the field
    mapped_disp_plane = ops.mapping.on_coordinates(fields_container=my_disp,
                                                   coordinates=my_plane.mesh.nodes.coordinates_field,
                                                   create_support=True,
                                                   mesh=my_meshed_region
                                                   ).eval()[0]

Plot displacement field on the plane
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plot displacement field on the |Plane| and display mesh in background.
Create the plotter and add fields and meshes. For more information about
plotting data on a mesh check the tutorial: :ref:`ref_plotting_data_on_the_mesh`

First, define the |DpfPlotter| object [2]_, then add |MeshedRegion|
to it using the |add_mesh| method and add the field using the |add_field| method.

To display the figure built by the plotter object use the |show_figure| method.

.. code-block:: python

    # Declare the DpfPlotter object
    my_plotter = dpf.plotter.DpfPlotter()
    # Add the MeshedRegion to the DpfPlotter object
    # We use custom style for the mesh so we can visualise the points
    my_plotter.add_mesh(meshed_region=my_meshed_region,style="surface", show_edges=True, color="w", opacity=0.3)
    # Add the Field to the DpfPlotter object
    my_plotter.add_field(field=mapped_disp_plane, meshed_region=my_plane.mesh, show_edges=False)
    # Display the plot
    my_plotter.show_figure(show_axes=True, cpos=camera_position)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    mapped_disp_plane = ops.mapping.on_coordinates(fields_container=my_disp,
                                                   coordinates=my_plane.mesh.nodes.coordinates_field,
                                                   create_support=True,
                                                   mesh=my_meshed_region
                                                   ).eval()[0]
    my_plotter = dpf.plotter.DpfPlotter()
    my_plotter.add_mesh(meshed_region=my_meshed_region,style="surface", show_edges=True, color="w", opacity=0.3)
    my_plotter.add_field(field=mapped_disp_plane, meshed_region=my_plane.mesh, show_edges=False)
    my_plotter.show_figure(show_axes=True, cpos=camera_position)

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
