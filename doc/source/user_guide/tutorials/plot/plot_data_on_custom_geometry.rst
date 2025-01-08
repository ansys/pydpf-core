.. _ref_plot_data_on_custom_geometry:

============================
Plot data on custom geometry
============================

.. |add_mesh| replace:: :func:`add_mesh()<ansys.dpf.core.plotter.DpfPlotter.add_mesh>`
.. |add_field| replace:: :func:`add_field()<ansys.dpf.core.plotter.DpfPlotter.add_field>`
.. |show_figure| replace:: :func:`show_figure()<ansys.dpf.core.plotter.DpfPlotter.show_figure>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |Line| replace:: :class:`Line <ansys.dpf.core.geometry.Line>`
.. |Points| replace:: :class:`Points <ansys.dpf.core.geometry.Points>`
.. |Plane| replace:: :class:`Plane <ansys.dpf.core.geometry.Plane>`
.. |mapping| replace:: :class:`mapping <ansys.dpf.core.operators.mapping.on_coordinates.on_coordinates>`
.. |nodes_coordinates| replace:: :class:`nodes_coordinates<ansys.dpf.core.operators.mesh.node_coordinates.node_coordinates>`
.. |Points.plot| replace:: :func:`Points.plot()<ansys.dpf.core.geometry.Points.plot>`
.. |Line.plot| replace:: :func:`Line.plot()<ansys.dpf.core.geometry.Line.plot>`
.. |Plane.plot| replace:: :func:`Plane.plot()<ansys.dpf.core.geometry.Plane.plot>`

This tutorials shows how to get a result mapped over different geometric objects:

- Points
- Line
- Plane

:jupyter-download-script:`Download tutorial as Python script<plot_data_on_custom_geometry>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<plot_data_on_custom_geometry>`

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
    # Import the geometry module
    from ansys.dpf.core import geometry as geo

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

Extract the results to be plotted on the geometry elements. Here, we get the displacement results.

.. jupyter-execute::

    # Get the displacement results
    disp_results = model_1.results.displacement.eval()

To a better visualization of the mesh and the geometry elements, we define a camera position.
A camera position is a combination of:

- A position;
- A focal point (the target);
- A upwards vector.

It results in a list of format:

.. code-block:: python

   camera_position= [[pos_x, pos_y, pos_z],  # position
                     [fp_x, fp_y, fp_z],  # focal point
                     [up_x, up_y, up_z]]  # upwards vector

.. jupyter-execute::

    # Define the camera position
    camera_position = [
    (0.07635352356975698, 0.1200500294271993, 0.041072502929096165),
    (0.015, 0.045, 0.015),
    (-0.16771051558419411, -0.1983722658245161, 0.9656715938216944),
    ]

Create the geometry elements
----------------------------

The geometry elements must be in the space domain of the mesh. You can verify the range of coordinates
values by checking the nodes coordinates.

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


.. tab-set::

    .. tab-item:: Points

        Create |Points| by defining their coordinates.

        The coordinates are define at the global Cartesian coordinates system by default. Thus, combining
        the max and min coordinates gives us the points that are in the corner of the mesh. We can also
        place one point in the middle of the mesh by calculating the middle distance between the coordinates.

        You can do it by hand or by calculating this combinations.

        .. jupyter-execute::

            # Define the coordinates of the point on the middle of the mesh
            # 1) Get the distance between the max and min coordinates
            distance_minmax_coords = ops.math.minus(fieldA=max_coords.data_as_list, fieldB=min_coords.data_as_list).eval()
            # 2) Get the middle of that distance
            middle = ops.math.scale(field=distance_minmax_coords, ponderation=0.5).eval()
            # 3) Find the coordinate to the point on the middle of the mesh
            middle_coords = ops.math.add(fieldA=min_coords.data_as_list,fieldB=middle.data_as_list).eval()

            # Define the points coordinates
            pts = geo.Points(coordinates=[
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

    .. tab-item:: Line

        Create a |Line| passing through the mesh diagonal. To create a |Line|
        you must define:

        - The coordinates of the starting point
        - The coordinates of the ending point
        - The number of points where the |Line| object will be discretized.

        .. jupyter-execute::

            # Create the Line object
            line_1 = geo.Line(coordinates=[[0.0, 0.06, 0.0], [0.03, 0.03, 0.03]],
                               n_points=50
                               )

    .. tab-item:: Plane

        Create a vertical |Plane| passing through the mesh mid point. To create a |Plane|
        you must define:

        - The coordinates of the point in the center of the plane
        - The vector of the normal direction to the plane
        - The plane width (x direction)
        - The plane height (y direction)
        - The number of cells (x and y direction) where the |Plane| object will be discretized.

        .. jupyter-execute::

            # Define the coordinates of the point on the middle of the mesh
            # 1) Get the distance between the max and min coordinates
            distance_minmax_coords = ops.math.minus(fieldA=max_coords.data_as_list, fieldB=min_coords.data_as_list).eval()
            # 2) Get the middle of that distance
            middle = ops.math.scale(field=distance_minmax_coords, ponderation=0.5).eval()
            # 3) Find the coordinate to the point on the middle of the mesh
            middle_coords = ops.math.add(fieldA=min_coords.data_as_list,fieldB=middle.data_as_list).eval()

            # Create the Plane object
            plane_1 = geo.Plane(center=middle_coords.data_as_list,
                                normal=[1, 1, 0],
                                width=0.03,
                                height=0.03,
                                n_cells_x=10,
                                n_cells_y=10,
                                )

Plot the geometry elements on the mesh
--------------------------------------

.. tab-set::

    .. tab-item:: Points

        You can plot the |Points| objects on the mesh using the |Points.plot| method [1]_.

        .. jupyter-execute::

            # Display the mesh and the points
            pts.plot(mesh=meshed_region_1, cpos=camera_position)

    .. tab-item:: Line

        You can plot the |Line| object on the mesh using the |Line.plot| method [1]_.

        .. jupyter-execute::

            # Display the mesh and the line
            line_1.plot(mesh=meshed_region_1, cpos=camera_position)

    .. tab-item:: Plane

        You can plot the |Plane| object on the mesh using the |Plane.plot| method [1]_.

        .. jupyter-execute::

            # Display the mesh and the plane
            plane_1.plot(mesh=meshed_region_1, cpos=camera_position)

Map the results to the geometry elements
----------------------------------------

Map the displacement results to the geometry elements using the |mapping| operator. This operator
retrieves the results of the entities located in the given coordinates (The path coordinates have to be in
the space domain of the mesh). If the given coordinates don't match with any entity coordinate, the operator
interpolates the results inside elements with shape functions.

The displacement results are defined in a *`nodal`* location. Thus, each node has a coordinate in the
mesh and a corresponding displacement data.

.. tab-set::

    .. tab-item:: Points

        The |mapping| operator takes the coordinates stored in a |Field|. Thus, we must create a |Field| with the
        |Points| coordinates.

        .. jupyter-execute::

            # Create the coordinates field
            points_coords_field = dpf.fields_factory.field_from_array(arr=pts.coordinates.data)

            # Map the points coordinates with the displacement results
            mapped_disp_points = ops.mapping.on_coordinates(fields_container=disp_results,
                                                            coordinates=points_coords_field,
                                                            create_support=True,
                                                            mesh=meshed_region_1
                                                            ).eval()[0]

    .. tab-item:: Line

        The |mapping| operator takes the coordinates stored in a |Field|. Thus, we must create a |Field| with the
        |Line| coordinates.

        .. jupyter-execute::

            # Get the coordinates field
            line_coords_field = line_1.mesh.nodes.coordinates_field

            # Map the line coordinates with the displacement results
            mapped_disp_line = ops.mapping.on_coordinates(fields_container=disp_results,
                                                          coordinates=line_coords_field,
                                                          create_support=True,
                                                          mesh=meshed_region_1
                                                           ).eval()[0]

    .. tab-item:: Plane

        The |mapping| operator takes the coordinates stored in a |Field|. Thus, we must create a |Field| with the
        |Plane| coordinates.

        .. jupyter-execute::

            # Get the coordinates field
            plane_coords_field = plane_1.mesh.nodes.coordinates_field

            # Map the plane coordinates with the displacement results
            mapped_disp_plane = ops.mapping.on_coordinates(fields_container=disp_results,
                                                          coordinates=plane_coords_field,
                                                          create_support=True,
                                                          mesh=meshed_region_1
                                                           ).eval()[0]

Plot the results on the geometry elements
-----------------------------------------

To plot the results on the path, we use the |DpfPlotter| object. For more information about
plotting data on a mesh, see the :ref:`ref_plot_data_on_a_mesh` tutorial.

First, define the |DpfPlotter| object [2]_. Next, add the |MeshedRegion|
and the |Field| containing the results using the |add_mesh| and |add_field| methods respectively.

To display the figure built by the plotter object use the |show_figure| method.

.. tab-set::

    .. tab-item:: Points

        .. jupyter-execute::

            # Define the DpfPlotter object
            plotter_1 = dpf.plotter.DpfPlotter()

            # Add the MeshedRegion to the DpfPlotter object
            # We use custom style for the mesh so we can visualize the path (that is inside the mesh)
            plotter_1.add_mesh(meshed_region=meshed_region_1,
                               style="surface",show_edges=True, color="w", opacity=0.3)

            # Add the Field to the DpfPlotter object
            plotter_1.add_field(field=mapped_disp_points,
                                point_size=20.0,
                                render_points_as_spheres=True)

            # Display the plot
            plotter_1.show_figure(show_axes=True,
                                  cpos=camera_position)

    .. tab-item:: Line

        .. jupyter-execute::

            # Define the DpfPlotter object
            plotter_2 = dpf.plotter.DpfPlotter()

            # Add the MeshedRegion to the DpfPlotter object
            # We use custom style for the mesh so we can visualize the path (that is inside the mesh)
            plotter_2.add_mesh(meshed_region=meshed_region_1,
                               style="surface",show_edges=True, color="w", opacity=0.3)

            # Add the Field to the DpfPlotter object
            plotter_2.add_field(field=mapped_disp_line)

            # Display the plot
            plotter_2.show_figure(show_axes=True,
                                  cpos=camera_position)

    .. tab-item:: Plane

        .. jupyter-execute::

            # Define the DpfPlotter object
            plotter_3 = dpf.plotter.DpfPlotter()

            # Add the MeshedRegion to the DpfPlotter object
            # We use custom style for the mesh so we can visualize the path (that is inside the mesh)
            plotter_3.add_mesh(meshed_region=meshed_region_1,
                               style="surface",show_edges=True, color="w", opacity=0.3)

            # Add the Field to the DpfPlotter object
            plotter_3.add_field(field=mapped_disp_plane,
                                meshed_region=plane_1.mesh,
                                show_edges=False)

            # Display the plot
            plotter_3.show_figure(show_axes=True,
                                  cpos=camera_position)

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
