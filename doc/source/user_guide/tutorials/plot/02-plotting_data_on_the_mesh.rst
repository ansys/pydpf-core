.. _ref_plotting_data_on_the_mesh:

=========================
Plotting data on the mesh
=========================


.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |plot| replace:: :func:`plot()<ansys.dpf.core.field.Field.plot>`
.. |DpfPlotter| replace:: :class:`DpfPlotter<ansys.dpf.core.plotter.DpfPlotter>`

This tutorial shows how to plot data on its supporting mesh by different approaches.

Define the data
---------------

In this tutorial we will download a pontoon simulation result file available
in our ``Examples`` package:

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples file
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    # Define the result file
    pontoon_file = examples.download_pontoon()

The |Model| is a helper designed to give shortcuts to access the analysis results
metadata, by opening a DataSources or a Streams, and to instanciate results provider for it.

Printing the model displays the available results.

.. code-block:: python

    # Create the model
    my_model = dpf.Model(data_sources=pontoon_file)
    # Print the model
    print(my_model)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    pontoon_file = examples.download_pontoon()
    my_model = dpf.Model(data_sources=pontoon_file)
    print(my_model)

We need to extract the data we want to plot. Mind that the results location must be of
type ``Elemental`` or ``Nodal``. Fot more information about extracting results from a
result file check the ":ref:`ref_tutorials_import_data`" tutorials section.

Here we choose to get the elastic strain.

.. code-block:: python

    # Extract the elastic strain result
    my_elastic_strain = my_model.results.elastic_strain.eval()
    # Print the result
    print(my_elastic_strain)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_elastic_strain = my_model.results.elastic_strain.eval()
    print(my_elastic_strain)

As the elastic strain result is in a ``ElementalNodal`` location we have to change it.
Here we define the new location with a input of the
:class:`elastic_strain() <ansys.dpf.core.operators.result.elastic_strain.elastic_strain>` operator.
Another option would be using an averaging operator like the
:class:`to_nodal_fc() <ansys.dpf.core.operators.averaging.to_nodal_fc.to_nodal_fc>` operator

.. code-block:: python

    # Define the desired location as an input of the results operator
    my_elastic_strain.inputs.requested_location(dpf.locations.nodal)
    # Get the result field
    # As we have only one time step we got a FieldsContainer with one Field (index=0)
    fc_elastic_strain = my_elastic_strain.eval()
    # Print the result
    print(fc_elastic_strain)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    my_elastic_strain.inputs.requested_location(dpf.locations.nodal)
    fc_elastic_strain = my_elastic_strain.eval()
    print(fc_elastic_strain)

Plot the data on the mesh
-------------------------

To plot the data on the mesh you have two different approaches:

    1)  :ref:`method_plot_data_mesh_1`
    2)  :ref:`method_plot_data_mesh_2`

For both approaches we need a |MeshedRegion| to base on. We can define it from the |Model|:

.. code-block:: python

    # Define the meshed region
    my_meshed_region = my_model.metadata.meshed_region

.. _method_plot_data_mesh_1:

Plot the Field on its mesh support
----------------------------------

To plot
.. warning::

    The |plot| method for the Field object is primarily added out of convenience as plotting
    directly from the field can be slower than extracting the meshed region and plotting the
    field on top of that.

Once we extract the field with the elastic strain results we can plot it on its
supporting mesh using the |plot| method:

.. code-block:: python

    # Define the field
    field_elastic_strain = fc_elastic_strain[0]
    # Use the plot() method
    field_elastic_strain.plot(meshed_region=my_meshed_region)

.. _method_plot_data_mesh_2:

Plot the mesh and add the field
-------------------------------

