.. _ref_plotting_data_on_the_mesh:

=========================
Plotting data on the mesh
=========================

.. |Field.plot| replace:: :func:`Field.plot()<ansys.dpf.core.field.Field.plot>`
.. |MeshedRegion.plot| replace:: :func:`MeshedRegion.plot()<ansys.dpf.core.meshed_region.MeshedRegion.plot>`
.. |add_mesh| replace:: :func:`add_mesh()<ansys.dpf.core.plotter.DpfPlotter.add_mesh>`
.. |add_field| replace:: :func:`add_field()<ansys.dpf.core.plotter.DpfPlotter.add_field>`
.. |show_figure| replace:: :func:`show_figure()<ansys.dpf.core.plotter.DpfPlotter.show_figure>`
.. |to_nodal_fc| replace:: :class:`to_nodal_fc() <ansys.dpf.core.operators.averaging.to_nodal_fc.to_nodal_fc>`
.. |select_component| replace:: :func:`select_component() <ansys.dpf.core.fields_container.FieldsContainer.select_component>`

This tutorial shows how to plot data on its supporting mesh by different approaches.

:jupyter-download-script:`Download tutorial as Python script<plotting_data_on_the_mesh>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<plotting_data_on_the_mesh>`

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

    # Define the result file path
    result_file_path_1 = examples.find_multishells_rst()

The |Model| is a helper designed to give shortcuts to access the analysis results
metadata and to instanciate results providers by opening a |DataSources| or a Streams.

Printing the model displays the available results.

.. jupyter-execute::

    # Create the model
    model_1 = dpf.Model(data_sources=result_file_path_1)

    # Print the model
    print(model_1)

Extract the data to be plotted. For more information about extracting results from a result file,
see the :ref:`ref_tutorials_import_data` tutorials section.

.. note::

     Only the *'elemental'* or *'nodal'* locations are supported for  plotting.

Here, we chose to plot the XX stress tensor component data.

First, get the stress |Result| object.

.. jupyter-execute::

    # Extract the stress Result
    stress_result = model_1.results.stress()

    # Print the results
    print(stress_result.eval())

We must request the stress in a *'nodal'* location as the default *'ElementalNodal'* location for the stress results
is not supported for plotting.

There are different ways to change the location. Here, we define the new location using the input of the stress
|Result|. Another option would be using an averaging operator, like the |to_nodal_fc| operator

.. jupyter-execute::

    # Define the desired location as an input of the result operator
    stress_result.inputs.requested_location(dpf.locations.nodal)

    # Get the output (here a FieldsContainer)
    fc_stress = stress_result.eval()

    # Print the output
    print(fc_stress)

To get the results for the XX stress component, we use the |select_component| method. This methods takes
the index the component as an input. The stress tensor has 6 components per elementary data
(symmetrical tensor XX,YY,ZZ,XY,YZ,XZ). Thus, we get the component of index=0

.. jupyter-execute::

    # Get the stress results for the XX component
    fc_stress_XX = fc_stress.select_component(index=0)

Plot the data on the mesh
-------------------------

There are two different approaches to plot the data on the mesh:

- :ref:`method_plot_data_mesh_1`
- :ref:`method_plot_data_mesh_2`

.. hint::

    :ref:`method_plot_data_mesh_2` is faster than :ref:`method_plot_data_mesh_1`

For both approaches, you need a |MeshedRegion| to be based on. Here, we get a |MeshedRegion| from
a result file. For more information about how to extract a |MeshedRegion| from a result file, see the
:ref:`ref_tutorials_get_mesh_from_result_file` tutorial.

.. jupyter-execute::

    # Define the meshed region
    meshed_region_1 = model_1.metadata.meshed_region

.. _method_plot_data_mesh_1:

Plot the data on its mesh support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plotting the data in DPF means plotting the |Field| or |FieldsContainer| that contains the data.
To plot a |Field|, you can use:

- :ref:`The Field.plot() method <ref_plot_field_on_mesh_plot_method_1>`;
- :ref:`The DpfPlotter object <ref_plot_field_on_mesh_DpfPlotter_1>`.

.. hint::

    Using the |DpfPlotter| class is faster than using the |Field.plot| method

.. _ref_plot_field_on_mesh_plot_method_1:

Using the plot() method
~~~~~~~~~~~~~~~~~~~~~~~

First, get a |Field| from the stress results |FieldsContainer|. Then, use the |Field.plot| method [1]_.
You have to use the *'meshed_region'* argument and give the Field supporting mesh.

.. jupyter-execute::

    # Define the field
    field_stress_XX = fc_stress_XX[0]

    # Plot the data on the mesh
    field_stress_XX.plot(meshed_region=meshed_region_1)

.. _ref_plot_field_on_mesh_DpfPlotter_1:

Using the DpfPlotter class
~~~~~~~~~~~~~~~~~~~~~~~~~~

First define the |DpfPlotter| object [2]_. Then, add the |Field| to it using the |add_field| method.
You must use the *'meshed_region'* argument and give the Field supporting mesh.

To display the figure built by the plotter object, use the |show_figure| method.

.. jupyter-execute::

    # Define the DpfPlotter object
    plotter_1 = dpf.plotter.DpfPlotter()

    # Add the Field and MeshedRegion to the DpfPlotter object
    plotter_1.add_field(field=field_stress_XX, meshed_region=meshed_region_1)

    # Display the plot
    plotter_1.show_figure()

.. _method_plot_data_mesh_2:

Plot the mesh and add the data on top of that
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To extract the meshed region and plot the |Field| on top of that you can use:

- :ref:`The MeshedRegion.plot() method <ref_plot_field_on_mesh_plot_method_2>`;
- :ref:`The DpfPlotter object <ref_plot_field_on_mesh_DpfPlotter_2>`.

For this approach, you can use the data from a |Field| or from a |FieldsContainer|.

.. hint::

    The |DpfPlotter| class is faster than using the |MeshedRegion.plot| method.

.. _ref_plot_field_on_mesh_plot_method_2:

Using the plot() method
~~~~~~~~~~~~~~~~~~~~~~~

Use the |MeshedRegion.plot| method [1]_. You must use the *'field_or_fields_container'* argument and
give the |Field| or the |FieldsContainer| containing the stress results data.

Use a |Field| containing the data.

.. jupyter-execute::

    # Plot the stress results
    meshed_region_1.plot(field_or_fields_container=field_stress_XX)

Use a |FieldsContainer| containing the data.

.. jupyter-execute::

    # Plot the stress results
    meshed_region_1.plot(field_or_fields_container=fc_stress_XX)

.. _ref_plot_field_on_mesh_DpfPlotter_2:

Using the DpfPlotter class
~~~~~~~~~~~~~~~~~~~~~~~~~~

First, define the |DpfPlotter| object [2]_. Then, add the |MeshedRegion|
to it, using the |add_mesh| method, and the |Field|, using the |add_field| method.

To display the figure built by the plotter object use the |show_figure| method.

.. jupyter-execute::

    # Declare the DpfPlotter object
    plotter_2 = dpf.plotter.DpfPlotter()

    # Add the MeshedRegion to the DpfPlotter object
    plotter_2.add_mesh(meshed_region=meshed_region_1)

    # Add the Field to the DpfPlotter object
    plotter_2.add_field(field=field_stress_XX)

    # Display the plot
    plotter_2.show_figure()

.. rubric:: Footnotes

.. [1] The default plotter settings display the mesh with edges, lighting and axis widget enabled.
Nevertheless, as we use the `PyVista <pyVista_github_>`_ library to create the plot, you can use additional
PyVista arguments (available at :func:`pyvista.plot`), such as:

.. jupyter-execute::

    field_stress_XX.plot(title= "Field Stress",
                         text= "Fields plot() method"  # Adds the given text at the bottom of the plot
                         )
    # Notes:
    # - To save a screenshot to file, use "screenshot=figure_name.png" ( as well as "notebook=False" if on a Jupyter notebook).
    # - The "off_screen" keyword only works when "notebook=False". If "off_screen=True" the plot is not displayed when running the code.

.. [2] The |DpfPlotter| object is currently a PyVista based object.
That means that PyVista must be installed, and that it supports kwargs as
parameter (the argument must be supported by the installed PyVista version).
More information about the available arguments are available at `pyvista.plot() <pyvista_doc_plot_method_>`_`.

The default |DpfPlotter| object settings displays the mesh with edges and lighting
enabled. Nevertheless, as we use the `PyVista <pyVista_github_>`_
library to create the plot, you can use additional PyVista arguments for the |DpfPlotter|
object and |add_field| method (available at `pyvista.plot() <pyvista_doc_plot_method_>`_`).