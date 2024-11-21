.. _reft_tutorials_narrow_down_data:

================
Narrow down data
================

.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`
.. |Scoping| replace:: :class:`Scoping<ansys.dpf.core.scoping.Scoping>`
.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |time_freq_scoping_factory| replace:: :mod:`time_freq_scoping_factory<ansys.dpf.core.time_freq_scoping_factory>`
.. |mesh_scoping_factory| replace:: :mod:`mesh_scoping_factory<ansys.dpf.core.mesh_scoping_factory>`
.. |Model| replace:: :class:`Model <ansys.dpf.core.model.Model>`
.. |displacement| replace:: :class:`result.displacement <ansys.dpf.core.operators.result.displacement.displacement>`
.. |Model.results| replace:: :func:`Model.results <ansys.dpf.core.model.Model.results>`
.. |Examples| replace:: :mod:`Examples<ansys.dpf.core.examples>`
.. |result op| replace:: :mod:`result<ansys.dpf.core.operators.result>`
.. |Result| replace:: :class:`Result <ansys.dpf.core.results.Result>`
.. |rescope| replace:: :class:`rescope <ansys.dpf.core.operators.scoping.rescope.rescope>`
.. |from_mesh| replace:: :class:`from_mesh <ansys.dpf.core.operators.scoping.from_mesh.from_mesh>`
.. |extract_scoping| replace:: :class:`extract_scoping <ansys.dpf.core.operators.utility.extract_scoping.extract_scoping>`

To begin the workflow set up, you need to establish the ``scoping``, that is
a spatial and/or temporal subset of the simulation data. This tutorial explains
how to scope your results over time and mesh domains.

Understanding a scope
---------------------

The data in DPF is represented by a |Field|. Thus, narrow down your results means scoping your |Field|.
To do so in DPF you use the |Scoping| object.

.. note::

    Scoping is important because when DPF-Core returns the |Field| object, what Python actually has
    is a client-side representation of the |Field|, not the entirety of the |Field| itself. This means
    that all the data of the field is stored within the DPF service. This is important
    because when building your workflows, the most efficient way of interacting with result data
    is to minimize the exchange of data between Python and DPF, either by using operators
    or by accessing exclusively the data that is needed.

For more information on the DPF data storage structures see :ref:`ref_tutorials_data_structures`.

The |Field| scoping also defines how the data is ordered, for example: the first
ID in the scoping identifies to which entity the first data entity belongs.

In conclusion, the essence of the scoping is to specify the set of time or mesh entities by defining a range of IDs:

.. image:: ../../../images/drawings/scoping-eg.png
   :align: center

Create a |Scoping|
------------------

The |Scoping| object can be created by:

- Instantiating the |Scoping| class (giving the location and the entities ids as arguments)
- Using a scoping factory (|time_freq_scoping_factory| methods for a temporal scoping
  and |mesh_scoping_factory| for spatial scoping).

.. code-block:: python

    # Import the ``ansys.dpf.core`` module
    from ansys.dpf import core as dpf

Time scoping
^^^^^^^^^^^^

.. code-block:: python

    # 1) Using the Scoping class
    # a. Define a time list that targets the times ids 14, 15, 16, 17
    my_time_list_1 = [14, 15, 16, 17]
    # b. Create the time scoping object
    my_time_scoping_1 = dpf.Scoping(ids=my_time_list_1, location=dpf.locations.time_freq)

    # 2) Using the time_freq_scoping_factory class
    # a. Define a time list that targets the times ids 14, 15, 16, 17
    my_time_list_2 = [14, 15, 16, 17]
    # b. Create the time scoping object
    my_time_scoping_2 = dpf.time_freq_scoping_factory.scoping_by_sets(cumulative_sets=my_time_list_2)

Mesh scoping
^^^^^^^^^^^^

.. code-block:: python

    # 1) Using the Scoping class in a nodal location
    # a. Define a nodes list that targets the nodes with the ids 103, 204, 334, 1802
    my_nodes_ids_1 = [103, 204, 334, 1802]
    # b. Create the mesh scoping object
    my_mesh_scoping_1 = dpf.Scoping(ids=my_nodes_ids_1, location=dpf.locations.nodal)

    # 2) Using the mesh_scoping_factory class
    # a. Define a nodes list that targets the nodes with the ids 103, 204, 334, 1802
    my_nodes_ids_2 = [103, 204, 334, 1802]
    # b. Create the mesh scoping object
    my_mesh_scoping_2 = dpf.mesh_scoping_factory.nodal_scoping(node_ids=my_nodes_ids_2)

Extract a |Scoping|
-------------------

A mesh |Scoping| can be extracted from:

- A |MeshedRegion| with the |from_mesh| operator;
- A |FieldsContainer| with the |extract_scoping| operator;
- A |Field| with the |extract_scoping| operator.


Get the results file
^^^^^^^^^^^^^^^^^^^^

Here we will download a  result file available in our |Examples| package.
For more information about how to import your result file in DPF check
the :ref:`ref_tutorials_import_result_file` tutorial.

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops

    # Define the result file
    result_file_path_1 = examples.download_transient_result()
    # Create the model
    my_model_1 = dpf.Model(data_sources=result_file_path_1)
    # Get the meshed region
    my_meshed_region_1 = my_model_1.metadata.meshed_region
    # Get a FieldsContainer
    my_fc = my_model_1.results.displacement.on_all_time_freqs.eval()
    # Get a Field
    my_field = my_fc[0]

Extract the |Scoping|
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # 3) Extract the scoping from a mesh
    my_mesh_scoping_3 = ops.scoping.from_mesh(mesh=my_meshed_region_1).eval()
    print("Scoping from mesh", "\n", my_mesh_scoping_3, "\n")

    # 4) Extract the scoping from a FieldsContainer
    extract_scop_fc_op = ops.utility.extract_scoping(field_or_fields_container=my_fc)
    my_mesh_scoping_4 = extract_scop_fc_op.outputs.mesh_scoping_as_scopings_container()
    print("Scoping from FieldsContainer", "\n", my_mesh_scoping_4, "\n")

    # 5) Extract the scoping from a Field
    my_mesh_scoping_5 = ops.utility.extract_scoping(field_or_fields_container=my_field).eval()
    print("Scoping from Field", "\n", my_mesh_scoping_5, "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    # Define the result file
    result_file_path_1 = examples.download_transient_result()
    # Create the model
    my_model_1 = dpf.Model(data_sources=result_file_path_1)
    # Get the meshed region
    my_meshed_region_1 = my_model_1.metadata.meshed_region
    # Get a FieldsContainer
    my_fc = my_model_1.results.displacement.on_all_time_freqs.eval()
    # Get a Field
    my_field = my_fc[0]
    # 3) Extract the scoping from a mesh
    my_mesh_scoping_3 = ops.scoping.from_mesh(mesh=my_meshed_region_1).eval()
    print("Scoping from mesh", "\n", my_mesh_scoping_3, "\n")

    # 4) Extract the scoping from a FieldsContainer
    extract_scop_fc_op = ops.utility.extract_scoping(field_or_fields_container=my_fc)
    my_mesh_scoping_4 = extract_scop_fc_op.outputs.mesh_scoping_as_scopings_container()
    print("Scoping from FieldsContainer", "\n", my_mesh_scoping_4, "\n")

    # 5) Extract the scoping from a Field
    my_mesh_scoping_5 = ops.utility.extract_scoping(field_or_fields_container=my_field).eval()
    print("Scoping from Field", "\n", my_mesh_scoping_5, "\n")

Use a |Scoping|
---------------

The |Scoping| object can be used :

- As an input to a |result op|  operator;
- As an |Result| argument when you extract results using the |Model.results| method;
- With the |Result| object methods.

The mesh scoping can also be changed after the result extraction or manipulation by using the
|rescope| operator with a |Field| or |FieldsContainer|.

Get the results file
^^^^^^^^^^^^^^^^^^^^

Here we will download a  result file available in our |Examples| package.
For more information about how to import your result file in DPF check
the :ref:`ref_tutorials_import_result_file` tutorial.

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops

    # Define the result file
    result_file_path_1 = examples.download_transient_result()
    # Create the DataSources object
    my_data_sources_1 = dpf.DataSources(result_path=result_file_path_1)
    # Create the model
    my_model_1 = dpf.Model(data_sources=my_data_sources_1)

Extract and scope the results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here we extract and scope the displacement results.

.. code-block:: python

    # 1) Using the result.displacement operator
    disp_op = ops.result.displacement(data_sources=my_data_sources_1,
                                      time_scoping=my_time_scoping_1,
                                      mesh_scoping=my_mesh_scoping_1).eval()

    # 2) Using the Model.results
    disp_model = my_model_1.results.displacement(time_scoping=my_time_scoping_1, mesh_scoping=my_mesh_scoping_1).eval()

    # 3) Using a Result object method
    disp_result_method_1 = my_model_1.results.displacement.on_time_scoping(time_scoping=my_time_scoping_1).on_mesh_scoping(mesh_scoping=my_mesh_scoping_1).eval()
    disp_result_method_2 = my_model_1.results.displacement.on_first_time_freq.eval()

    print("Displacement from result.displacement operator", "\n", disp_op, "\n")
    print("Displacement from Model.results ", "\n", disp_model, "\n")
    print("Scoping from Result object method 1", "\n", disp_result_method_1, "\n")
    print("Scoping from Result object method 1", "\n", disp_result_method_2, "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops

    # Define the result file
    result_file_path_1 = examples.download_transient_result()
    # Create the DataSources object
    my_data_sources_1 = dpf.DataSources(result_path=result_file_path_1)
    # Create the model
    my_model_1 = dpf.Model(data_sources=my_data_sources_1)
    my_time_list_1 = [14, 15, 16, 17]
    my_time_scoping_1 = dpf.Scoping(ids=my_time_list_1, location=dpf.locations.time_freq)
    my_nodes_ids_1 = [103, 204, 334, 1802]
    my_mesh_scoping_1 = dpf.Scoping(ids=my_nodes_ids_1, location=dpf.locations.nodal)
    # 1) Using the result.displacement operator
    disp_op = ops.result.displacement(data_sources=my_data_sources_1,
                                      time_scoping=my_time_scoping_1,
                                      mesh_scoping=my_mesh_scoping_1).eval()

    # 2) Using the Model.results
    disp_model = my_model_1.results.displacement(time_scoping=my_time_scoping_1, mesh_scoping=my_mesh_scoping_1).eval()

    # 3) Using a Result object method
    disp_result_method_1 = my_model_1.results.displacement.on_time_scoping(time_scoping=my_time_scoping_1).on_mesh_scoping(mesh_scoping=my_mesh_scoping_1).eval()
    disp_result_method_2 = my_model_1.results.displacement.on_first_time_freq.eval()

    print("Displacement from result.displacement operator", "\n", disp_op, "\n")
    print("Displacement from Model.results ", "\n", disp_model, "\n")
    print("Scoping from Result object method 1", "\n", disp_result_method_1, "\n")
    print("Scoping from Result object method 1", "\n", disp_result_method_2, "\n")

Extract and rescope the results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here we rescope the displacement results.

.. code-block:: python

    # 1) Extract the results for the entire mesh
    disp_all_mesh = my_model_1.results.displacement.eval()

    # 2) Rescope the displacement results
    disp_rescope = ops.scoping.rescope(fields=disp_all_mesh, mesh_scoping=my_mesh_scoping_1).eval()

    print("Displacement on all the mesh", "\n", disp_all_mesh, "\n")
    print("Displacement rescoped ", "\n", disp_rescope, "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    disp_all_mesh = my_model_1.results.displacement.eval()
    disp_rescope = ops.scoping.rescope(fields=disp_all_mesh, mesh_scoping=my_mesh_scoping_1).eval()
    print("Displacement on all the mesh", "\n", disp_all_mesh, "\n")
    print("Displacement rescoped ", "\n", disp_rescope, "\n")