.. _ref_tutorials_plot_contour:

===================
Plot data on a mesh
===================

.. |Field.plot| replace:: :func:`Field.plot()<ansys.dpf.core.field.Field.plot>`
.. |MeshedRegion.plot| replace:: :func:`MeshedRegion.plot()<ansys.dpf.core.meshed_region.MeshedRegion.plot>`
.. |add_mesh| replace:: :func:`add_mesh()<ansys.dpf.core.plotter.DpfPlotter.add_mesh>`
.. |add_field| replace:: :func:`add_field()<ansys.dpf.core.plotter.DpfPlotter.add_field>`
.. |show_figure| replace:: :func:`show_figure()<ansys.dpf.core.plotter.DpfPlotter.show_figure>`
.. |to_nodal_fc| replace:: :class:`to_nodal_fc <ansys.dpf.core.operators.averaging.to_nodal_fc.to_nodal_fc>`
.. |select_component| replace:: :func:`select_component() <ansys.dpf.core.fields_container.FieldsContainer.select_component>`
.. |stress_op| replace:: :class:`stress <ansys.dpf.core.operators.result.stress.stress>`

.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`
.. |Model| replace:: :py:class:`Model <ansys.dpf.core.model.Model>`
.. |Examples| replace:: :py:mod:`Examples<ansys.dpf.core.examples>`
.. |MeshedRegion| replace:: :py:class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |MeshesContainer| replace:: :py:class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>`
.. |DpfPlotter| replace:: :py:class:`DpfPlotter<ansys.dpf.core.plotter.DpfPlotter>`

This tutorial shows different commands for plotting data contours on a mesh.

:jupyter-download-script:`Download tutorial as Python script<plot_data_on_a_mesh>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<plot_data_on_a_mesh>`

Load data to plot
-----------------

For this tutorial, we use mesh information and data from a case available in the |Examples| module.
For more information on how to import your own result file in DPF, see
the :ref:`ref_tutorials_import_data` tutorials section.

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module
    import ansys.dpf.core as dpf
    # Import the examples module
    from ansys.dpf.core import examples

    # Define the result file path
    result_file_path_1 = examples.download_piston_rod()

    # Create a model from the result file
    model_1 = dpf.Model(data_sources=result_file_path_1)

Plot a contour on a single mesh
-------------------------------

Get the mesh
^^^^^^^^^^^^

Here we simply get the |MeshedRegion| object of the model, but any other |MeshedRegion| works.

.. jupyter-execute::

    # Extract the mesh
    meshed_region_1 = model_1.metadata.meshed_region

Get data to plot
^^^^^^^^^^^^^^^^

Extract data for the contour. For more information about extracting results from a result file,
see the :ref:`ref_tutorials_import_data` tutorials section.

.. note::

     Only the *'elemental'* or *'nodal'* locations are supported for  plotting.

Here, we chose to plot the XX stress tensor component data.

First, get the stress results using the |stress_op| operator.

.. jupyter-execute::

    # Extract the stress results
    stress_result = model_1.results.stress()

    # Print the results
    print(stress_result.eval())

We must request the stress in a *'nodal'* location as the default *'ElementalNodal'* location for the stress results
is not supported for plotting.

There are different ways to change the location. Here, we define the new location using the input of the |stress_op|
operator. Another option would be using an averaging operator, like the |to_nodal_fc| operator

.. jupyter-execute::

    # Define the desired location as an input of the stress operator
    stress_result.inputs.requested_location(dpf.locations.nodal)

    # Get the output (here a FieldsContainer)
    fc_stress = stress_result.eval()

To get the results for the XX stress component, we use the |select_component| method. This methods takes
the index the component as an input. The stress tensor has 6 components per elementary data
(symmetrical tensor XX,YY,ZZ,XY,YZ,XZ). Thus, we get the component of index=0

.. jupyter-execute::

    # Get the stress results for the XX component
    fc_stress_XX = fc_stress.select_component(index=0)

Plot the contour
^^^^^^^^^^^^^^^^

There are two different approaches to plot the data on the mesh:

- :ref:`Plot the data on its mesh support <ref_method_plot_data_mesh_1>`
- :ref:`Plot the mesh and add the data on top of that <ref_method_plot_data_mesh_2>`

.. hint::

    :ref:`ref_method_plot_data_mesh_2` is faster than :ref:`ref_method_plot_data_mesh_1`


.. _ref_method_plot_data_mesh_1:

Plot the data on its mesh support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plotting the data in DPF means plotting the |Field| that contains the data.
To plot a |Field|, you can use:

- The |Field.plot| method;
- The |DpfPlotter| object.

.. hint::

    Using the |DpfPlotter| class is faster than using the |Field.plot| method

.. tab-set::

    .. tab-item:: Field.plot() method

        First, get a |Field| from the stress results |FieldsContainer|. Then, use the |Field.plot| method [1]_.
        If the |Field| does not have a predefined mesh support, you must use the *'meshed_region'* argument and
        give the |Field| supporting mesh.

        .. jupyter-execute::

            # Define the field
            field_stress_XX = fc_stress_XX[0]

            # Plot the data on the mesh
            field_stress_XX.plot(meshed_region=meshed_region_1)

    .. tab-item:: DpfPlotter object

        First define the |DpfPlotter| object [2]_. Then, add the |Field| to it using the |add_field| method.
        If the |Field| does not have a predefined mesh support, you must use the *'meshed_region'* argument
        and give the |Field| supporting mesh.

        To display the figure built by the plotter object, use the |show_figure| method.

        .. jupyter-execute::

            # Define the DpfPlotter object
            plotter_1 = dpf.plotter.DpfPlotter()

            # Add the Field and MeshedRegion to the DpfPlotter object
            plotter_1.add_field(field=field_stress_XX, meshed_region=meshed_region_1)

            # Display the plot
            plotter_1.show_figure()

.. _ref_method_plot_data_mesh_2:

Plot the mesh and add the data on top of that
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To plot the |MeshedRegion| and add the data on top of that you can use:

- The |MeshedRegion.plot| method;
- The |DpfPlotter| object.

.. hint::

    The |DpfPlotter| class is faster than using the |MeshedRegion.plot| method.

.. tab-set::

    .. tab-item:: MeshedRegion.plot() method

        For this approach, you can use data stored in a |Field| or in a |FieldsContainer|.
        In this tutorial, we use data stored in a |Field|.

        Use the |MeshedRegion.plot| method [1]_. You must use the *'field_or_fields_container'* argument and
        give the |Field| or the |FieldsContainer| containing the stress results data.

        .. jupyter-execute::

            # Plot the mesh and add the stress results
            meshed_region_1.plot(field_or_fields_container=field_stress_XX)

    .. tab-item:: DpfPlotter object

        First, define the |DpfPlotter| object [2]_. Then, add the |MeshedRegion|
        and the |Field| using the |add_mesh| and |add_field| methods respectively.

        To display the figure built by the plotter object use the |show_figure| method.

        .. jupyter-execute::

            # Define the DpfPlotter object
            plotter_2 = dpf.plotter.DpfPlotter()

            # Add the MeshedRegion to the DpfPlotter object
            plotter_2.add_mesh(meshed_region=meshed_region_1)

            # Add the Field to the DpfPlotter object
            plotter_2.add_field(field=field_stress_XX)

            # Display the plot
            plotter_2.show_figure()

Plot a contour on a collection of meshes
----------------------------------------

Build a collection of meshes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get data to plot on the meshes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plot the data contour
^^^^^^^^^^^^^^^^^^^^^

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