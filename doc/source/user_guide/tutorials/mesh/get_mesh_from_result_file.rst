.. _tutorials_get_mesh_from_result_file:

=============================
Get a mesh from a result file
=============================

.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.field.Field>`
.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |DataSources| replace:: :class:`Model <ansys.dpf.core.data_sources.DataSources>`
.. |mesh_provider| replace:: <ansys.dpf.core.operators.mesh.mesh_provider.mesh_provider>`

The mesh object in DPF is a |MeshedRegion|. You can obtain a |MeshedRegion| by creating your
own by scratch or by getting it from a result file.

This tutorial explains how to extract the models mesh from a result file.


Import the result file
----------------------

Here we we will download a  result file available in our `Examples` package.
For more information about how to import your result file in DPF check
the :ref:`ref_tutorials_import_data` tutorial section.

You have to create a |DataSources| object so the data can be accessed by
PyDPF-Core APIs.

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    # Define the result file
    result_file_path = examples.find_static_rst()
    # Create the DataSources object
    my_data_sources = dpf.DataSources(result_path=result_file_path)

Get the mesh from the result file
---------------------------------

You can Get the mesh from the result file by two methods:

- :ref:`get_mesh_model`
- :ref:`get_mesh_mesh_provider`

.. note::

    The |Model| extracts a large amount of information by default (results, mesh and analysis data).
    If using this helper takes a long time for processing the code, mind using a |DataSources| object
    and instantiating operators directly with it. Check the ":ref:`get_mesh_mesh_provider`" for more
    information on how to get a mesh from a result file.

.. _get_mesh_model:

Using the DPF |Model|
^^^^^^^^^^^^^^^^^^^^^

The |Model| is a helper designed to give shortcuts to access the analysis results
metadata, by opening a DataSources or a Streams, and to instanciate results provider
for it.

Get the |MeshedRegion| by instantiating a |Model| object and accessing its metadata:

.. code-block:: python

    # Create the model
    my_model = dpf.Model(data_sources=my_data_sources)
    # Get the mesh
    my_meshed_region_1 = my_model.metadata.meshed_region

Printing the |MeshedRegion| displays the mesh dimensions (number of nodes and elements,
unit and elements type):

.. code-block:: python

    # Print the meshed region
    print(my_meshed_region_1)

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    result_file_path = examples.find_static_rst()
    my_data_sources = dpf.DataSources(result_path=result_file_path)
    my_model = dpf.Model(data_sources=my_data_sources)
    my_meshed_region_1 = my_model.metadata.meshed_region
    print(my_meshed_region_1)

.. _get_mesh_mesh_provider:

Using the |mesh_provider| operator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get the |MeshedRegion| by instantiating the |mesh_provider| operator and instantiating it with a
|DataSources| object as an argument:

.. code-block:: python

    # Get the mesh with the mesh_provider operator
    my_meshed_region_2 = ops.mesh.mesh_provider(data_sources=my_data_sources).eval()

Printing the |MeshedRegion| displays the mesh dimensions (number of nodes and elements,
unit and elements type):

.. code-block:: python

    # Print the meshed region
    print(my_meshed_region_2)