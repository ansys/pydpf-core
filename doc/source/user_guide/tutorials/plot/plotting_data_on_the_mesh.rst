.. _ref_plotting_data_on_the_mesh:

=========================
Plotting data on the mesh
=========================


.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |plot| replace:: :func:`plot()<ansys.dpf.core.field.Field.plot>`
.. |plotMesh| replace:: :func:`plot()<ansys.dpf.core.meshed_region.MeshedRegion.plot>`
.. |DpfPlotter| replace:: :class:`DpfPlotter<ansys.dpf.core.plotter.DpfPlotter>`
.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.field.Field>`

This tutorial shows how to plot data on its supporting mesh by different approaches.

Define the data
---------------

In this tutorial we will download a simulation result file available
in our ``Examples`` package:

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples file
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    # Define the result file
    result_file = examples.find_multishells_rst()

The |Model| is a helper designed to give shortcuts to access the analysis results
metadata, by opening a DataSources or a Streams, and to instanciate results provider for it.

Printing the model displays the available results.

.. code-block:: python

    # Create the model
    my_model = dpf.Model(data_sources=result_file)
    # Print the model
    print(my_model)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    result_file = examples.find_multishells_rst()
    my_model = dpf.Model(data_sources=result_file)
    print(my_model)

We need to extract the data we want to plot. Mind that the results location must be of
type ``Elemental`` or ``Nodal``. Fot more information about extracting results from a
result file check the :ref:`ref_tutorials_import_data` tutorials section.

Here we choose to get the XX stress tensor component result. We start by extracting the stress results:

.. code-block:: python

    # Extract the stress result
    my_stress = my_model.results.stress()
    # Print the result
    print(my_stress.eval())

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_stress = my_model.results.stress()
    print(my_stress.eval())

As the stress result is in a ``ElementalNodal`` location we have to change it
(for plotting the location needs to be of type ``Elemental`` or ``Nodal``).

Here we define the new location with a input of the
:class:`stress() <ansys.dpf.core.operators.result.stress.stress>` operator.
Another option would be using an averaging operator like the
:class:`to_nodal_fc() <ansys.dpf.core.operators.averaging.to_nodal_fc.to_nodal_fc>` operator

.. code-block:: python

    # Define the desired location as an input of the results operator
    my_stress.inputs.requested_location(dpf.locations.nodal)
    # Get the result (the stress result operator gives an FieldsContainer as an output)
    fc_stress = my_stress.eval()
    # Print the result
    print(fc_stress)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_stress.inputs.requested_location(dpf.locations.nodal)
    fc_stress = my_stress.eval()
    print(fc_stress)

To get the results only for the XX stress component we have to use
the :func:`select_component() <ansys.dpf.core.fields_container.FieldsContainer.select_component>`
method:

.. code-block:: python

    # Define the component to get.
    # The stress tensor has 6 components per elementary data (symmetrical tensor XX,YY,ZZ,XY,YZ,XZ).
    # So we get the component of index=0
    fc_stress_XX = fc_stress.select_component(index=0)

Plot the data on the mesh
-------------------------

To plot the data on the mesh you have two different approaches:

    1)  :ref:`method_plot_data_mesh_1`
    2)  :ref:`method_plot_data_mesh_2`

.. hint::

    :ref:`method_plot_data_mesh_2` is faster than :ref:`method_plot_data_mesh_1`

For both approaches we need a |MeshedRegion| to base on. We can define it from the |Model|:

.. code-block:: python

    # Define the meshed region
    my_meshed_region = my_model.metadata.meshed_region

.. _method_plot_data_mesh_1:

Plot the data on its mesh support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plotting the data in DPF means plotting the |Field| or |FieldsContainer| that contains the data.
To plot a |Field| you can use the |plot| method or the |DpfPlotter| class.

.. hint::

    The |DpfPlotter| class is faster than using the |plot| method

Using the plot() method
~~~~~~~~~~~~~~~~~~~~~~~

First, extract the Field with the stress results. Then use the |plot| method [1]_.
You have to give the Fields supporting mesh as a attribute:

.. code-block:: python

    # Define the field
    field_stress_XX = fc_stress_XX[0]
    # Use the plot() method
    field_stress_XX.plot(meshed_region=my_meshed_region)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    fc_stress_XX = fc_stress.select_component(index=0)
    my_meshed_region = my_model.metadata.meshed_region
    field_stress_XX = fc_stress_XX[0]
    field_stress_XX.plot(meshed_region=my_meshed_region)

Using the DpfPlotter class
~~~~~~~~~~~~~~~~~~~~~~~~~~

First you have to define the |DpfPlotter| object [2]_ and then add the Field
to it using the :func:`add_field()<ansys.dpf.core.plotter.DpfPlotter.add_field>` method.
You have to give the Fields supporting mesh as an attribute to this method.

To display the figure built by the plotter object you need to use the
:func:`show_figure()<ansys.dpf.core.plotter.DpfPlotter.show_figure>`  method.

.. code-block:: python

    # Declare the DpfPlotter object
    my_plotter = dpf.plotter.DpfPlotter()
    # Add the MeshedRegion to the DpfPlotter object
    my_plotter.add_field(field=field_stress_XX, meshed_region=my_meshed_region)
    # Display the plot
    my_plotter.show_figure()

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_plotter = dpf.plotter.DpfPlotter()
    my_plotter.add_field(field=field_stress_XX, meshed_region=my_meshed_region)
    my_plotter.show_figure()



.. _method_plot_data_mesh_2:

Plot the mesh and add the data on top of that
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To extract the meshed region and plot the |Field| on top of that you can use the |plotMesh|
method or the |DpfPlotter| class.

In this approach you can add the data from a |Field| or from a |FieldsContainer|.

.. hint::

    The |DpfPlotter| class is faster than using the |plotMesh| method.

Using the plot() method
~~~~~~~~~~~~~~~~~~~~~~~

Use the |plotMesh| method [1]_ with the meshed region we extracted from the model.
You have to give the Field or the FieldsContainer with the stress data as a attribute:

.. code-block:: python

    # Use the plot() method with a Field as an attribute
    my_meshed_region.plot(field_or_fields_container=field_stress_XX)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_meshed_region.plot(field_or_fields_container=field_stress_XX)

.. code-block:: python

    # Use the plot() method with a FieldsContainer as an attribute
    my_meshed_region.plot(field_or_fields_container=fc_stress_XX)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_meshed_region.plot(field_or_fields_container=fc_stress_XX)

Using the DpfPlotter class
~~~~~~~~~~~~~~~~~~~~~~~~~~

First you have to define the |DpfPlotter| object [2]_ and then add |MeshedRegion|
to it using the :func:`add_mesh()<ansys.dpf.core.plotter.DpfPlotter.add_mesh>` method and add the
field using the :func:`add_field()<ansys.dpf.core.plotter.DpfPlotter.add_field>` method.

To display the figure built by the plotter object use the
:func:`show_figure()<ansys.dpf.core.plotter.DpfPlotter.show_figure>`  method.

.. code-block:: python

    # Declare the DpfPlotter object
    my_plotter = dpf.plotter.DpfPlotter()
    # Add the MeshedRegion to the DpfPlotter object
    my_plotter.add_mesh(meshed_region=my_meshed_region)
    # Add the Field to the DpfPlotter object
    my_plotter.add_field(field=field_stress_XX)
    # Display the plot
    my_plotter.show_figure()

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_plotter = dpf.plotter.DpfPlotter()
    my_plotter.add_mesh(meshed_region=my_meshed_region)
    my_plotter.add_field(field=field_stress_XX)
    my_plotter.show_figure()

.. rubric:: Footnotes

.. [1] The default plotter settings display the mesh with edges, lighting and axis widget enabled.
Nevertheless, as we use the `PyVista <https://github.com/pyvista/pyvista>`_ library to create
the plot you can use additional PyVista arguments (available at: :func:`pyvista.plot`), such as:

.. code-block:: python

    field_stress_XX.plot(title= "Field Stress",
                         text= "Fields plot() method"  # Adds the given text at the bottom of the plot
                         )
    # Notes:
    # - To save a screenshot to file, use "screenshot=figure_name.png" ( as well as "notebook=False" if on a Jupyter notebook).
    # - The "off_screen" keyword only works when "notebook=False". If "off_screen=True" the plot is not displayed when running the code.

.. [2] Here we use the |DpfPlotter| object, that is currently a PyVista based object.
That means that PyVista must be installed, and that it supports kwargs as
parameter (the argument must be supported by the installed PyVista version).

The default |DpfPlotter| object settings display the mesh with edges and lighting
enabled. Nevertheless, as we use the `PyVista <https://github.com/pyvista/pyvista>`_
library to create the plot you can use additional PyVista arguments for the |DpfPlotter|
object and :func:`add_field()<ansys.dpf.core.plotter.DpfPlotter.add_field>` method
(available at: :func:`pyvista.plot`).