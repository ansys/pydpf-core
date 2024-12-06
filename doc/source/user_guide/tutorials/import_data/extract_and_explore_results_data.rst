.. _ref_tutorials_extract_and_explore_results_data:

================================
Extract and explore results data
================================

.. include:: ../../../links_and_refs.rst
.. |get_entity_data| replace:: :func:`get_entity_data()<ansys.dpf.core.field.Field.get_entity_data>`
.. |get_entity_data_by_id| replace:: :func:`get_entity_data_by_id()<ansys.dpf.core.field.Field.get_entity_data_by_id>`

This tutorial shows how to extract and explore results data from a result file.

When you extract a result from a result file DPF stores it in a |Field|.
Thus, this |Field| contains the data of the result associated with it.

.. note::

    When DPF-Core returns the |Field| object, what Python actually has is a client-side
    representation of the |Field|, not the entirety of the |Field| itself. This means
    that all the data of the field is stored within the DPF service. This is important
    because when building your workflows, the most efficient way of interacting with result data
    is to minimize the exchange of data between Python and DPF, either by using operators
    or by accessing exclusively the data that is needed.

:jupyter-download-script:`Download tutorial as Python script<extract_and_explore_results_data>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<extract_and_explore_results_data>`

Get the result file
-------------------

First, import a result file. For this tutorial, you can use one available in the |Examples| module.
For more information about how to import your own result file in DPF, see the :ref:`ref_tutorials_import_result_file`
tutorial.

Here, we extract the displacement results. The displacement |Result| object gives a |FieldsContainer| when evaluated.
Thus, we get a |Field| from this |FieldsContainer|.

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module
    from ansys.dpf import core as dpf
    # Import the examples module
    from ansys.dpf.core import examples
    # Import the operators module
    from ansys.dpf.core import operators as ops

    # Define the result file path
    result_file_path_1 = examples.download_transient_result()

    # Create the model
    model_1 = dpf.Model(data_sources=result_file_path_1)

    # Extract the displacement results for the last time step
    disp_results = model_1.results.displacement.on_last_time_freq.eval()

    # Get the displacement field for the last time step
    disp_field = disp_results[0]

    # Print the displacement Field
    print(disp_field)

Extract all the data from a |Field|
-----------------------------------

You can extract the entire data in a |Field| as:

- An array (numpy array);
- A list.

Data as an array
^^^^^^^^^^^^^^^^

.. jupyter-execute::

    # Get the displacement data as an array
    data_array = disp_field.data

    # Print the data as an array
    print("Displacement data as an array: ", '\n', data_array)

Note that this array is a genuine, local, numpy array (overloaded by the DPFArray):

.. jupyter-execute::

    # Print the array type
    print("Array type: ", type(data_array))

Data as a list
^^^^^^^^^^^^^^

.. jupyter-execute::

    # Get the displacement data as a list
    data_list = disp_field.data_as_list
    # Print the data as a list
    print("Displacement data as a list: ", '\n', data_list)

Extract specific data from a field
----------------------------------

If you need to access data for specific entities (node, element ...), you can extract it with two approaches:

- :ref:`Based on its index <ref_extract_specific_data_by_index>` (data position on the |Field|) by using the |get_entity_data| method;
- :ref:`Based on the entities id <ref_extract_specific_data_by_id>` by using the |get_entity_data_by_id| method.

The |Field| data is organized with respect to its scoping ids. Note that the element with id=533
would correspond to an index=2 within the |Field|.

.. jupyter-execute::

    # Get the index of the entity with id=533
    index_533_entity = disp_field.scoping.index(id=533)
    # Print the index
    print("Index entity id=533: ",index_533_entity)

Be aware that scoping IDs are not sequential. You would get the id of the element in the 533
position of the |Field| with:

.. jupyter-execute::

    # Get the id of  the entity with index=533
    id_533_entity = disp_field.scoping.id(index=533)
    print("Id entity index=533: ",id_533_entity)

.. _ref_extract_specific_data_by_index:

Get the data by the entity index
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::

    # Get the data from the third entity in the field
    data_3_entity = disp_field.get_entity_data(index=3)
    # Print the data
    print("Data entity index=3: ", data_3_entity)

.. _ref_extract_specific_data_by_id:

Get the data by the entity id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::

    # Get the data from the entity with id=533
    data_533_entity = disp_field.get_entity_data_by_id(id=533)
    # Print the data
    print("Data entity id=533: ", data_533_entity)

Extract specific data from a field using a loop over the array
--------------------------------------------------------------

While the methods above are acceptable when requesting data for a few elements
or nodes, they should not be used when looping over the entire array. For efficiency,
a |Field| data can be recovered locally before sending a large number of requests:

.. jupyter-execute::

    # Create a deep copy of the field that can be accessed and modified locally.
    with disp_field.as_local_field() as f:
        for i in disp_field.scoping.ids[2:50]:
            f.get_entity_data_by_id(i)

    # Print the field
    print(f)