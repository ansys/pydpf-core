.. _ref_tutorials_extract_and_explore_results_metadata:

========================
Explore results metadata
========================

.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |Examples| replace:: :mod:`Examples<ansys.dpf.core.examples>`
.. |ResultInfo| replace:: :class:`ResultInfo<ansys.dpf.core.result_info.ResultInfo>`

You can explore the general results metadata before extracting them by using
the |ResultInfo| object. This metadata includes:

- Analysis type;
- Physics type;
- Number of results;
- Unit system;
- Solver version, date and time;
- Job name;

When you extract a result from a result file DPF stores it in a |Field|.
This |Field| will then contain the metadata for the result associated with it.
This metadata includes:

- Location;
- Scoping;
- Shape of the data stored;
- Number of components;
- Units of the data.

This tutorial shows how to extract and explore results metadata from a result file.

Get the result file
-------------------

Here we will download a  result file available in our |Examples| package.
For more information about how to import your result file in DPF check
the :ref:`ref_tutorials_import_result_file` tutorial.

Here we get the displacement results.

.. code-block:: python

    # Import the ``ansys.dpf.core`` module, including examples files and the operators subpackage
    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops

    # Define the result file
    result_file_path_1 = examples.download_transient_result()
    # Create the model
    my_model_1 = dpf.Model(data_sources=result_file_path_1)

Explore the general results metadata
------------------------------------

Get the |ResultInfo| object from the model and then explore it using this class methods.

.. code-block:: python

    # Define the ResultInfo object
    my_result_info_1 = my_model_1.metadata.result_info

    # Get the analysis type
    my_analysis_type = my_result_info_1.analysis_type
    print("Analysis type: ",my_analysis_type, "\n")

    # Get the physics type
    my_physics_type = my_result_info_1.physics_type
    print("Physics type: ",my_physics_type, "\n")

    # Get the number of available results
    number_of_results = my_result_info_1.n_results
    print("Number of available results: ",number_of_results, "\n")

    # Get the unit system
    my_unit_system = my_result_info_1.unit_system
    print("Unit system: ",my_unit_system, "\n")

    # Get the solver version, data and time
    my_solver_version = my_result_info_1.solver_version
    print("Solver version: ",my_solver_version, "\n")

    my_solver_date = my_result_info_1.solver_date
    print("Solver date: ", my_solver_date, "\n")

    my_solver_time = my_result_info_1.solver_time
    print("Solver time: ",my_solver_time, "\n")

    # Get the job name
    my_job_name = my_result_info_1.job_name
    print("Job name: ",my_job_name, "\n")

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    result_file_path_1 = examples.download_transient_result()
    my_model_1 = dpf.Model(data_sources=result_file_path_1)
    my_result_info_1 = my_model_1.metadata.result_info
    my_analysis_type = my_result_info_1.analysis_type
    print("Analysis type: ",my_analysis_type, "\n")
    my_physics_type = my_result_info_1.physics_type
    print("Physics type: ",my_physics_type, "\n")
    number_of_results = my_result_info_1.n_results
    print("Number of available results: ",number_of_results, "\n")
    my_unit_system = my_result_info_1.unit_system
    print("Unit system: ",my_unit_system, "\n")
    my_solver_version = my_result_info_1.solver_version
    print("Solver version: ",my_solver_version, "\n")
    my_solver_date = my_result_info_1.solver_date
    print("Solver date: ", my_solver_date, "\n")
    my_solver_time = my_result_info_1.solver_time
    print("Solver time: ",my_solver_time, "\n")
    my_job_name = my_result_info_1.job_name
    print("Job name: ",my_job_name, "\n")

Explore a given result metadata
-------------------------------

Here we will explore the metadata of the displacement results.

Start by extracting the displacement results:

.. code-block:: python

    # Extract the displacement results
    disp_results = my_model_1.results.displacement.eval()

    # Get the displacement field
    my_disp_field = disp_results[0]

Explore the displacement results metadata:

.. code-block:: python

    # Location of the displacement data
    my_location = my_disp_field.location
    print("Location: ", my_location,'\n')

    # Displacement field scoping
    my_scoping = my_disp_field.scoping  # type and quantity of entities
    print("Scoping: ", '\n',my_scoping, '\n')

    my_scoping_ids = my_disp_field.scoping.ids  # Available entities ids
    print("Scoping ids: ", my_scoping_ids, '\n')

    # Elementary data count
    # Number of entities (how many data vectors we have)
    my_elementary_data_count = my_disp_field.elementary_data_count
    print("Elementary data count: ", my_elementary_data_count, '\n')

    # Components count
    # Vectors dimension, here we have a displacement so we expect to have 3 components (X, Y and Z)
    my_components_count = my_disp_field.component_count
    print("Components count: ", my_components_count, '\n')

    # Size
    # Length of the data entire vector (equal to the number of elementary data times the number of components)
    my_field_size = my_disp_field.size
    print("Size: ", my_field_size, '\n')

    # Fields shape
    # Gives a tuple with the elementary data count and the components count
    my_shape = my_disp_field.shape
    print("Shape: ", my_shape, '\n')

    # Units
    my_unit = my_disp_field.unit
    print("Unit: ", my_unit, '\n')

.. rst-class:: sphx-glr-script-out

 .. jupyter-execute::
    :hide-code:

    # Extract the displacement results
    disp_results = my_model_1.results.displacement.eval()

    # Get the displacement field
    my_disp_field = disp_results[0]

    # Location of the displacement data
    my_location = my_disp_field.location
    print("Location: ", my_location,'\n')

    # Displacement field scoping
    my_scoping = my_disp_field.scoping  # type and quantity of entities
    print("Scoping: ", '\n',my_scoping, '\n')

    my_scoping_ids = my_disp_field.scoping.ids  # Available entities ids
    print("Scoping ids: ", my_scoping_ids, '\n')

    # Elementary data count
    # Number of entities (how many data vectors we have)
    my_elementary_data_count = my_disp_field.elementary_data_count
    print("Elementary data count: ", my_elementary_data_count, '\n')

    # Components count
    # Vectors dimension, here we have a displacement so we expect to have 3 components (X, Y and Z)
    my_components_count = my_disp_field.component_count
    print("Components count: ", my_components_count, '\n')

    # Size
    # Length of the data entire vector (equal to the number of elementary data times the number of components)
    my_field_size = my_disp_field.size
    print("Size: ", my_field_size, '\n')

    # Fields shape
    # Gives a tuple with the elementary data count and the components count
    my_shape = my_disp_field.shape
    print("Shape: ", my_shape, '\n')

    # Units
    my_unit = my_disp_field.unit
    print("Unit: ", my_unit, '\n')