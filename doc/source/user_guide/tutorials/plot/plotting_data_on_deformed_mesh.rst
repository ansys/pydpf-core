.. _ref_plotting_data_on_deformed_mesh:

==============================
Plotting data on deformed mesh
==============================

.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`
.. |MeshesContainer| replace:: :class:`MeshesContainer <ansys.dpf.core.meshes_container.MeshesContainer>`,

This tutorial shows how to plot data on the deformed mesh. For more detailed information  on plotting data
check the :ref:`ref_plotting_data_on_the_mesh` tutorial.

Define the data
---------------

In this tutorial we will download a simulation result file available
in our ``Examples`` package:

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module, including examples files and operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    # Define the result file
    result_file = examples.find_multishells_rst()

The |Model| is a helper designed to give shortcuts to access the analysis results
metadata, by opening a DataSources or a Streams, and to instanciate results provider for it.

Printing the model displays the available results.

.. jupyter-execute::

    # Create the model
    my_model = dpf.Model(data_sources=result_file)
    # Print the model
    print(my_model)


To deform the mesh we need a result with a homogeneous unit dimension, a distance unit.
Thus, to deform the mesh we need the displacement result.

Extract the displacements results from the model:

.. jupyter-execute::

    # Get the displacement results
    my_disp_result = my_model.results.displacement

We need to extract the data we want to plot on the deformed mesh.

Mind that the results location must be of type ``Elemental`` or ``Nodal``. We choose
to work with the XX stress tensor component result.

Fot more information about extracting results from a result file check
the :ref:`ref_tutorials_import_data` tutorials section.

.. jupyter-execute::

    # Extract the stress result
    my_stress = my_model.results.stress()

As the stress result is in a ``ElementalNodal`` location we have to change it.
Here we define the new location with a input of the
:class:`stress() <ansys.dpf.core.operators.result.stress.stress>` operator.

.. jupyter-execute::

    # Define the desired location as an input of the results operator
    my_stress.inputs.requested_location(dpf.locations.nodal)
    # Get the result (the stress result operator gives an FieldsContainer as an output)
    fc_stress = my_stress.eval()

To get the results only for the XX stress component we have to use
the :func:`select_component() <ansys.dpf.core.fields_container.FieldsContainer.select_component>`
method:

.. jupyter-execute::

    # Define the component to get.
    # The stress tensor has 6 components per elementary data (symmetrical tensor XX,YY,ZZ,XY,YZ,XZ).
    # So we get the component of index=0
    fc_stress_XX = fc_stress.select_component(index=0)

Plot deformed geometry
----------------------

Here we use the plot [1]_ method. For different approaches check the :ref:`ref_plotting_data_on_the_mesh` tutorial.

The geometry can be defined by a |MeshedRegion| or by a |MeshesContainer|.

Define the |MeshedRegion| from the |Model|:

.. jupyter-execute::

    # Define the meshed region
    my_meshed_region = my_model.metadata.meshed_region

There are different ways to obtain a |MeshesContainer|.

Here we get a |MeshesContainer| by using the :class:`split_mesh <ansys.dpf.core.operators.mesh.split_mesh.split_mesh>`
operator. It splits the mesh by material by default:

.. jupyter-execute::

    # Define the meshed region
    my_meshes = ops.mesh.split_mesh(mesh=my_meshed_region).eval()

The geometry can be deformed by a :class:`Result <ansys.dpf.core.results.Result>` object,
an :class:`Operator<ansys.dpf.core.dpf_operator.Operator>`, a :class:`Field<ansys.dpf.core.field.Field>`
or a :class:`FieldsContainer<ansys.dpf.core.field.Field>`.

The procedures are the same for a |MeshedRegion| and a |MeshesContainer|. For this reason we will show only
one plot for the |MeshesContainer|

.. jupyter-execute::

    # Define the plot formating
    my_scale_factor = 0.001
    my_window_size=[350,350]
    # Plot the XX stress tensor component results on a MeshedRegion deformed by:
    # a) a Result object
    my_meshed_region.plot( deform_by=my_disp_result,
                           scale_factor=my_scale_factor,
                           text="a",
                           window_size=my_window_size,)
    # b) an Operator
    my_disp_op = my_disp_result()
    my_meshed_region.plot( deform_by=my_disp_op,
                           scale_factor=my_scale_factor,
                           text="b",
                           window_size=my_window_size,)
    # c) a FieldsContainer
    my_disp_fc = my_disp_result.eval()
    my_meshed_region.plot( deform_by=my_disp_fc,
                           scale_factor=my_scale_factor,
                           text="c",
                           window_size=my_window_size,)
    # d) a Field
    my_disp_field = my_disp_fc[0]
    my_meshed_region.plot( deform_by=my_disp_field,
                           scale_factor=my_scale_factor,
                           text="d",
                           window_size=my_window_size)

    # Plot the XX stress tensor component results on a MeshesContainer deformed by a Field
    my_meshes.plot( deform_by=my_disp_field,
                           scale_factor=my_scale_factor,
                           text="e",
                           window_size=my_window_size)

Plot data on the deformed geometry
----------------------------------

Plot the data on its mesh support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plotting the data in DPF means plotting the |Field| that contains the data.

Plot the stress results on the deformed geometry:

.. jupyter-execute::

    # Define the stress field
    stress_field = fc_stress[0]
    # Plot the results on a deformed geometry. The data is in a Field
    stress_field.plot( deform_by=my_disp_field,
                        scale_factor=my_scale_factor)

Plot the mesh and add the stress data on top of that
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The data to be plotted in a |MeshedRegion| can be in a |Field|.

.. jupyter-execute::

    # Plot the MeshedRegion and the stress in a Field
    my_meshed_region.plot( field_or_fields_container=stress_field,
                           deform_by=my_disp_field,
                           scale_factor=my_scale_factor)


.. rubric:: Footnotes

.. [1] The default plotter settings display the mesh with edges, lighting and axis widget enabled.
Nevertheless, as we use the `PyVista <https://github.com/pyvista/pyvista>`_ library to create
the plot you can use additional PyVista arguments (available at: :func:`pyvista.plot`.





