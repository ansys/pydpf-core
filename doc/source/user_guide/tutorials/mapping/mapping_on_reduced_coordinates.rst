.. _ref_tutorials_mapping_on_reduced_coordinates:

============================
Reduced coordinates mapping
============================

.. |find_reduced_coordinates| replace:: :class:`find_reduced_coordinates<ansys.dpf.core.operators.mapping.find_reduced_coordinates>`
.. |on_reduced_coordinates| replace:: :class:`on_reduced_coordinates<ansys.dpf.core.operators.mapping.on_reduced_coordinates>`
.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer<ansys.dpf.core.fields_container.FieldsContainer>`
.. |Model| replace:: :class:`Model<ansys.dpf.core.model.Model>`
.. |fields_factory| replace:: :mod:`fields_factory<ansys.dpf.core.fields_factory>`

Perform high-precision interpolation at element-local coordinates.

This tutorial demonstrates a two-step mapping process that allows for high-precision
interpolation of field values at specific locations inside elements. This approach
differs from :ref:`ref_tutorials_mapping_on_coordinates` in that it first determines
the exact element and the local (reference) coordinates within that element, then
performs the interpolation. This is especially useful for advanced use cases such as
mapping at Gauss points or for mesh-to-mesh transfer where precise element-local
mapping is required.

:jupyter-download-script:`Download tutorial as Python script<mapping_on_reduced_coordinates>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<mapping_on_reduced_coordinates>`

Import modules and load the model
----------------------------------

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

Extract the mesh
----------------

Extract the mesh from the model, which is needed for finding reduced coordinates.

.. jupyter-execute::

    # Get the mesh from the model
    mesh = model.metadata.meshed_region

    # Print mesh information
    print(mesh)

Define target coordinates
-------------------------

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

Step 1: Find reduced coordinates and element IDs
-------------------------------------------------

Use the |find_reduced_coordinates| operator to locate which elements contain your
target coordinates and to compute the reduced (reference) coordinates within those elements.

.. jupyter-execute::

    # Create the find_reduced_coordinates operator
    find_op = ops.mapping.find_reduced_coordinates(
        coordinates=coords_field,
        mesh=mesh
    )

    # Evaluate the operator to get both outputs
    reduced_coords_fc = find_op.outputs.reduced_coordinates()
    element_ids_sc = find_op.outputs.element_ids()

    # Print the reduced coordinates
    print("Reduced coordinates:")
    print(reduced_coords_fc)

    # Print the element IDs
    print("\nElement IDs:")
    print(element_ids_sc)

Examine the reduced coordinates
--------------------------------

The reduced coordinates represent positions within the reference element coordinate system.

.. jupyter-execute::

    # Get the first field from the reduced coordinates FieldsContainer
    reduced_coords_field = reduced_coords_fc[0]

    # Print the reduced coordinates data
    print("Reduced coordinates data:")
    print(reduced_coords_field.data)

    # Get the element IDs scoping
    element_ids = element_ids_sc[0]

    # Print the element IDs
    print("\nElement IDs for each coordinate:")
    print(element_ids.ids)

Step 2: Map results to reduced coordinates
-------------------------------------------

Use the |on_reduced_coordinates| operator to interpolate field values at the found
reduced coordinates within the specified elements.

.. jupyter-execute::

    # Get displacement results
    displacement_fc = model.results.displacement.eval()

    # Print the displacement FieldsContainer
    print(displacement_fc)

.. jupyter-execute::

    # Create the on_reduced_coordinates operator
    mapping_op = ops.mapping.on_reduced_coordinates(
        fields_container=displacement_fc,
        reduced_coordinates=reduced_coords_fc,
        element_ids=element_ids_sc,
        mesh=mesh
    )

    # Evaluate the operator to get the mapped results
    mapped_displacement_fc = mapping_op.eval()

    # Print the resulting FieldsContainer
    print(mapped_displacement_fc)

Access mapped results
---------------------

Extract and display the interpolated displacement values.

.. jupyter-execute::

    # Get the first field from the mapped FieldsContainer
    mapped_field = mapped_displacement_fc[0]

    # Print the mapped field
    print(mapped_field)

    # Extract the data as a numpy array
    mapped_data = mapped_field.data

    # Print the interpolated displacement values
    print("\nInterpolated displacement values:")
    for i, point in enumerate(points):
        elem_id = element_ids.ids[i]
        print(f"Point {i+1} at {point} in element {elem_id}: displacement = {mapped_data[i]}")

Map stress results using the same reduced coordinates
-----------------------------------------------------

Once you have the reduced coordinates and element IDs, you can reuse them to map
different result types efficiently.

.. jupyter-execute::

    # Get stress results
    stress_fc = model.results.stress.eval()

    # Map stress using the same reduced coordinates and element IDs
    mapped_stress_fc = ops.mapping.on_reduced_coordinates(
        fields_container=stress_fc,
        reduced_coordinates=reduced_coords_fc,
        element_ids=element_ids_sc,
        mesh=mesh
    ).eval()

    # Print the mapped stress field
    print(mapped_stress_fc[0])

    # Extract stress data
    stress_data = mapped_stress_fc[0].data

    # Print stress values at each point
    print("\nInterpolated stress values:")
    for i, point in enumerate(points):
        elem_id = element_ids.ids[i]
        print(f"Point {i+1} at {point} in element {elem_id}: stress = {stress_data[i]}")

Use quadratic elements for higher precision
--------------------------------------------

If your mesh has quadratic elements, you can enable quadratic interpolation for
more precise results.

.. jupyter-execute::

    # Find reduced coordinates with quadratic element option
    find_op_quad = ops.mapping.find_reduced_coordinates(
        coordinates=coords_field,
        mesh=mesh,
        use_quadratic_elements=True
    )

    # Evaluate to get outputs
    reduced_coords_quad_fc = find_op_quad.outputs.reduced_coordinates()
    element_ids_quad_sc = find_op_quad.outputs.element_ids()

    # Map displacement with quadratic interpolation
    mapped_disp_quad_fc = ops.mapping.on_reduced_coordinates(
        fields_container=displacement_fc,
        reduced_coordinates=reduced_coords_quad_fc,
        element_ids=element_ids_quad_sc,
        mesh=mesh,
        use_quadratic_elements=True
    ).eval()

    # Print the result
    print("Displacement with quadratic interpolation:")
    print(mapped_disp_quad_fc[0].data)

When to use this approach
--------------------------

Use this two-step reduced coordinates approach when:

- You need precise mapping inside elements at specific element-local locations
- You are mapping at Gauss points or integration points
- You need mesh-to-mesh transfer with element-local accuracy
- The simple :ref:`ref_tutorials_mapping_on_coordinates` approach is not sufficient for your accuracy needs
- You want to reuse the same element-local positions for mapping multiple result types
