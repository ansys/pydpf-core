.. _ref_tutorials_extract_and_explore_results_metadata:

====================================
Extract and explore results metadata
====================================

.. include:: ../../../links_and_refs.rst
.. |ResultInfo| replace:: :class:`ResultInfo<ansys.dpf.core.result_info.ResultInfo>`

This tutorial shows how to extract and explore results metadata from a result file.

:jupyter-download-script:`Download tutorial as Python script<extract_and_explore_results_metadata>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<extract_and_explore_results_metadata>`

Get the result file
-------------------

First, import a result file. For this tutorial, you can use one available in the |Examples| module.
For more information about how to import your own result file in DPF, see the :ref:`ref_tutorials_import_result_file`
tutorial.

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

Explore the results general metadata
------------------------------------

You can explore the general results metadata, before extracting the results, by using
the |ResultInfo| object and its methods. This metadata includes:

- Analysis type;
- Physics type;
- Number of results;
- Unit system;
- Solver version, date and time;
- Job name;

.. jupyter-execute::

    # Define the ResultInfo object
    result_info_1 = model_1.metadata.result_info

    # Get the analysis type
    analysis_type = result_info_1.analysis_type
    # Print the analysis type
    print("Analysis type: ",analysis_type, "\n")

    # Get the physics type
    physics_type = result_info_1.physics_type
    # Print the physics type
    print("Physics type: ",physics_type, "\n")

    # Get the number of available results
    number_of_results = result_info_1.n_results
    # Print the number of available results
    print("Number of available results: ",number_of_results, "\n")

    # Get the unit system
    unit_system = result_info_1.unit_system
    # Print the unit system
    print("Unit system: ",unit_system, "\n")

    # Get the solver version, data and time
    solver_version = result_info_1.solver_version
    solver_date = result_info_1.solver_date
    solver_time = result_info_1.solver_time

    # Print the solver version, data and time
    print("Solver version: ",solver_version, "\n")
    print("Solver date: ", solver_date, "\n")
    print("Solver time: ",solver_time, "\n")

    # Get the job name
    job_name = result_info_1.job_name
    # Print the job name
    print("Job name: ",job_name, "\n")

Explore a result metadata
-------------------------
When you extract a result from a result file DPF stores it in a |Field|.
Thus, this |Field| contains the metadata for the result associated with it.
This metadata includes:

- Location;
- Scoping (type and quantity of entities);
- Elementary data count (number of entities, how many data vectors we have);
- Components count (vectors dimension, here we have a displacement so we expect to have 3 components (X, Y and Z));
- Shape of the data stored (tuple with the elementary data count and the components count);
- Fields size (length of the data entire vector (equal to the number of elementary data times the number of components));
- Units of the data.

Here we will explore the metadata of the displacement results.

Start by extracting the displacement results.

.. jupyter-execute::

    # Extract the displacement results
    disp_results = model_1.results.displacement.eval()

    # Get the displacement field
    disp_field = disp_results[0]

Explore the displacement results metadata:

.. jupyter-execute::

    # Get the location of the displacement data
    location = disp_field.location
    # Print the location
    print("Location: ", location,'\n')

    # Get the displacement Field scoping
    scoping = disp_field.scoping
    # Print the Field scoping
    print("Scoping: ", '\n',scoping, '\n')

    # Get the displacement Field scoping ids
    scoping_ids = disp_field.scoping.ids  # Available entities ids
    # Print the Field scoping ids
    print("Scoping ids: ", scoping_ids, '\n')

    # Get the displacement Field elementary data count
    elementary_data_count = disp_field.elementary_data_count
    # Print the elementary data count
    print("Elementary data count: ", elementary_data_count, '\n')

    # Get the displacement Field components count
    components_count = disp_field.component_count
    # Print the components count
    print("Components count: ", components_count, '\n')

    # Get the displacement Field size
    field_size = disp_field.size
    # Print the Field size
    print("Size: ", field_size, '\n')

    # Get the displacement Field shape
    shape = disp_field.shape
    # Print the Field shape
    print("Shape: ", shape, '\n')

    # Get the displacement Field unit
    unit = disp_field.unit
    # Print the displacement Field unit
    print("Unit: ", unit, '\n')