.. _ref_tutorials_mapping_on_coordinates:

============================
Interpolation at coordinates
============================

.. |on_coordinates| replace:: :class:`on_coordinates<ansys.dpf.core.operators.mapping.on_coordinates>`
.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`
.. |Model| replace:: :class:`Model<ansys.dpf.core.model.Model>`
.. |fields_factory| replace:: :mod:`fields_factory<ansys.dpf.core.fields_factory>`

Interpolate field values at arbitrary coordinates using shape functions.

This tutorial demonstrates how to use the |on_coordinates| operator to extract
result values at specific spatial locations in your model. The operator interpolates
field values at arbitrary coordinates using the mesh's shape functions, allowing
you to extract results along lines, at sensor locations, or on custom paths.

Any point outside the initial mesh returns an empty value.

:jupyter-download-script:`Download tutorial as Python script<mapping_on_coordinates>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<mapping_on_coordinates>`

Import modules and load the model
---------------------------------

First, import the required modules and load a result file.

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module
    from ansys.dpf import core as dpf

    # Import the examples module
    from ansys.dpf.core import examples

    # Import the operators module
    from ansys.dpf.core import operators as ops

    # Import numpy for coordinate manipulation
    import numpy as np

.. jupyter-execute::

    # Download and load a result file
    result_file = examples.find_static_rst()

    # Create a Model object
    model = dpf.Model(data_sources=result_file)

    # Print model information
    print(model)

Extract displacement results
----------------------------

Next, extract the displacement results from the model.

.. jupyter-execute::

    # Get displacement results as a FieldsContainer
    displacement_fc = model.results.displacement.eval()

    # Print the FieldsContainer information
    print(displacement_fc)

    # Print the first field
    print(displacement_fc[0])

Define coordinates of interest
------------------------------

Define the spatial coordinates where you want to interpolate results.

.. jupyter-execute::

    # Define points of interest as a numpy array
    # Each row represents one point with [x, y, z] coordinates
    points = np.array([
        [0.01, 0.04, 0.01],
        [0.02, 0.05, 0.02]
    ])

    # Create a Field from the array
    coords_field = dpf.fields_factory.field_from_array(arr=points)

    # Print the coordinates field
    print(coords_field)

Map displacement to coordinates
-------------------------------

Use the |on_coordinates| operator to interpolate displacement values at the defined coordinates.

.. jupyter-execute::

    # Create the on_coordinates operator
    mapping_op = ops.mapping.on_coordinates(
        fields_container=displacement_fc,
        coordinates=coords_field
    )

    # Evaluate the operator to get the mapped results
    mapped_displacement_fc = mapping_op.eval()

    # Print the resulting FieldsContainer
    print(mapped_displacement_fc)

Access mapped results
---------------------

Extract and display the interpolated displacement values.

.. jupyter-execute::

    # Get the first field from the FieldsContainer
    mapped_field = mapped_displacement_fc[0]

    # Print the mapped field
    print(mapped_field)

    # Extract the data as a numpy array
    mapped_data = mapped_field.data

    # Print the interpolated displacement values
    print("Interpolated displacement values:")
    print(mapped_data)

Map with mesh provided explicitly
---------------------------------

If the input fields do not have a mesh in their support, you can provide the mesh explicitly.

.. jupyter-execute::

    # Get the mesh from the model
    mesh = model.metadata.meshed_region

    # Create the on_coordinates operator with explicit mesh
    mapping_op_with_mesh = ops.mapping.on_coordinates(
        fields_container=displacement_fc,
        coordinates=coords_field,
        mesh=mesh
    )

    # Evaluate the operator
    mapped_displacement_with_mesh = mapping_op_with_mesh.eval()

    # Print the result
    print(mapped_displacement_with_mesh[0])

Adjust tolerance for coordinate search
--------------------------------------

You can adjust the tolerance used in the iterative algorithm to locate coordinates inside the mesh.

.. jupyter-execute::

    # Create the on_coordinates operator with custom tolerance
    # Default tolerance is 5e-5
    mapping_op_with_tol = ops.mapping.on_coordinates(
        fields_container=displacement_fc,
        coordinates=coords_field,
        tolerance=1e-4
    )

    # Evaluate the operator
    mapped_displacement_with_tol = mapping_op_with_tol.eval()

    # Print the result
    print(mapped_displacement_with_tol[0])

Map multiple result types
--------------------------

You can map different result types to the same coordinates.

.. jupyter-execute::

    # Get stress results
    stress_fc = model.results.stress.eval()

    # Map stress to the same coordinates
    mapped_stress_fc = ops.mapping.on_coordinates(
        fields_container=stress_fc,
        coordinates=coords_field
    ).eval()

    # Print the mapped stress field
    print(mapped_stress_fc[0])

Related examples
----------------

For practical applications of the ``on_coordinates`` operator, see:

- :ref:`stress_gradient_path` - Map stress results along a path normal to a node
- :ref:`plot_on_path` - Map and plot results along a defined coordinate path
- :ref:`plot_on_geometries` - Map fields to geometric objects (points, lines, planes)
