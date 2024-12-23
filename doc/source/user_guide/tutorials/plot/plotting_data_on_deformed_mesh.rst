.. _ref_plotting_data_on_deformed_mesh:

==============================
Plotting data on deformed mesh
==============================

.. |to_nodal_fc| replace:: :class:`to_nodal_fc() <ansys.dpf.core.operators.averaging.to_nodal_fc.to_nodal_fc>`
.. |select_component| replace:: :func:`select_component() <ansys.dpf.core.fields_container.FieldsContainer.select_component>`
.. |split_mesh| replace:: :class:`split_mesh <ansys.dpf.core.operators.mesh.split_mesh.split_mesh>`
.. |stress_op| replace:: :class:`stress <ansys.dpf.core.operators.result.stress.stress>`
.. |Field.plot| replace:: :func:`Field.plot()<ansys.dpf.core.field.Field.plot>`
.. |MeshedRegion.plot| replace:: :func:`MeshedRegion.plot()<ansys.dpf.core.meshed_region.MeshedRegion.plot>`

This tutorial shows how to plot data on the deformed mesh.

:jupyter-download-script:`Download tutorial as Python script<plotting_data_on_deformed_mesh>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<plotting_data_on_deformed_mesh>`

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
    result_file_path_1 = examples.find_multishells_rst()

The |Model| is a helper designed to give shortcuts to access the analysis results
metadata and to instanciate results providers by opening a |DataSources| or a Streams.

Printing the model displays the available results.

.. jupyter-execute::

    # Create the model
    model_1 = dpf.Model(data_sources=result_file_path_1)

    # Print the model
    print(model_1)

Extract the data to be plotted on the deformed mesh.

.. note::

     Only the *'elemental'* or *'nodal'* locations are supported for  plotting.

Here, we chose to plot the XX stress tensor component data. Thud, get the stress results using the |stress_op| operator.

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

Define the mesh
---------------

The mesh object in DPF is a |MeshedRegion|. You can store multiple |MeshedRegion| in a DPF collection
called |MeshesContainer|. Thus, the geometry can be defined by a |MeshedRegion| or by a |MeshesContainer|.

First, extract the |MeshedRegion| from the |Model|.

.. jupyter-execute::

    # Define the MeshedRegion
    meshed_region_1 = model_1.metadata.meshed_region

There are different ways to obtain a |MeshesContainer|. You can, for example, split a given |MeshedRegion| in different
parts.

Here, we get a |MeshesContainer| by splitting the |MeshedRegion| by material using the |split_mesh| operator.
This operator gives a |MeshesContainer| with the |MeshedRegion| split parts with a *'mat'* label.

.. jupyter-execute::

    # Define the MeshesContainer
    meshes_1 = ops.mesh.split_mesh(mesh=meshed_region_1).eval()

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
    disp_op = model_1.results.displacement()

Plot data on the deformed geometry
----------------------------------

Plotting the data in DPF means plotting the |Field| that contains the data.
Get a |Field| from the |FieldsContainer| containing the stress results .

.. jupyter-execute::

    # Define the field
    field_stress_XX = fc_stress_XX[0]

There are two different approaches to plot the data on the deformed mesh:

- :ref:`Plot the data on its mesh support <ref_method_plot_data_deformed_mesh_1>`;
- :ref:`Plot the mesh and add the stress data on top of that <ref_method_plot_data_deformed_mesh_2>`.

For all approaches, we use a scale factor so the deformed mesh fits properly on the plot.

.. jupyter-execute::

    # Define the scale factor
    scl_fct = 0.001

.. _ref_method_plot_data_deformed_mesh_1:

Plot the data on its mesh support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plotting the data in DPF means plotting the |Field| that contains the data.
To plot a |Field| on the deformed mesh, you can use:

- The |Field.plot| method;
- The |DpfPlotter| object.

Plot the stress results |Field| on the deformed geometry using the |Field.plot| method. Use the
*'deform_by'* argument and give the displacement results.

.. tab-set::

    .. tab-item:: Field.plot() method

        To plot the stress results in the deformed mesh, use the |Field.plot| method [1]_.
        Additionally, you must use the *'meshed_region'* and *'deform_by'* arguments and
        give the mesh and displacement results.

        .. jupyter-execute::

            # Plot the stress results on the deformed mesh
            field_stress_XX.plot(meshed_region=meshed_region_1,
                                 deform_by=disp_op,
                                 scale_factor=scl_fct)

    .. tab-item:: DpfPlotter object

        First define the |DpfPlotter| object [2]_. Then, add the |Field| to it using the |add_field| method.
        You must use the *'meshed_region'* and *'deform_by'* arguments and give the mesh and displacement results.

        To display the figure built by the plotter object, use the |show_figure| method.

        .. jupyter-execute::

            # Define the DpfPlotter object
            plotter_1 = dpf.plotter.DpfPlotter()

            # Add the Field and MeshedRegion to the DpfPlotter object
            plotter_1.add_field(field=field_stress_XX,
                                meshed_region=meshed_region_1,
                                deform_by=disp_op,
                                scale_factor=scl_fct)

            # Display the plot
            plotter_1.show_figure()

.. _ref_method_plot_data_deformed_mesh_2:

Plot the mesh and add the stress data on top of that
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To plot the deformed |MeshedRegion| and add the data on top of that you can use:

- The |MeshedRegion.plot| method;
- The |DpfPlotter| object.

.. hint::

    The |DpfPlotter| class is faster than using the |MeshedRegion.plot| method.

.. tab-set::

    .. tab-item:: MeshedRegion.plot() method

        For this approach, you can use data stored in a |Field| or in a |FieldsContainer|.
        In this tutorial, we use data stored in a |Field|.

        To plot the stress results in the deformed mesh, use the |MeshedRegion.plot| method [1]_.
        You must use the *'field_or_fields_container'* and *'deform_by'* arguments and give the
        stress and the displacement results.

        .. jupyter-execute::

            # Plot the deformed mesh and add the stress results
            meshed_region_1.plot(field_or_fields_container=field_stress_XX,
                                 deform_by=disp_op,
                                 scale_factor=scl_fct)

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



