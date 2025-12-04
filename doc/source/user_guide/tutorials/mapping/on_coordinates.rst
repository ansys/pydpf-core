.. _ref_tutorials_mapping_on_coordinates:

======================================
Mapping Results on Custom Coordinates
======================================

.. include:: ../../links_and_refs.rst

This tutorial shows how to map and interpolate field results onto custom coordinate locations using the :class:`on_coordinates operator <ansys.dpf.core.operators.mapping.on_coordinates>`.

This operator allows you to interpolate field data from a mesh to arbitrary spatial coordinates. This is particularly useful for extracting results along a path, transferring data between different meshes, or evaluating results at specific points of interest in your model.

:jupyter-download-script:`Download tutorial as Python script<on_coordinates>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<on_coordinates>`

Introduction to Mapping
------------------------

The :class:`mapping operator <ansys.dpf.core.operators.mapping.on_coordinates>` evaluates field results at specified coordinates by interpolating values inside elements using shape functions. This process involves:

- Locating which element contains each target coordinate
- Computing the position within the element using reduced (natural) coordinates
- Interpolating the field values using element shape functions

Key applications include:

- **Path extraction**: Extract results along a line or curve
- **Point probing**: Evaluate results at specific locations
- **Mesh-to-mesh transfer**: Map results between different meshes
- **Custom sampling**: Create custom result visualizations on user-defined grids

Set up the Analysis
-------------------

First, we import the required modules and load a static structural analysis result file.

.. jupyter-execute::

    # Import the ansys.dpf.core module
    from ansys.dpf import core as dpf

    # Import the examples module
    from ansys.dpf.core import examples

    # Import operators for convenience
    from ansys.dpf.core import operators as ops

    # Load a static analysis result file
    result_file_path = examples.find_static_rst()

    # Create a Model from the result file
    model = dpf.Model(result_file_path)

    # Get the mesh
    mesh = model.metadata.meshed_region

    # Display basic model information
    print(f"Number of nodes: {mesh.nodes.n_nodes}")
    print(f"Number of elements: {mesh.elements.n_elements}")
    print(f"Available results: {list(model.metadata.result_info.available_results.keys())[:5]}")

Extract Field Results
---------------------

Before mapping, we need to extract the field results we want to interpolate. Let's extract stress results.

.. jupyter-execute::

    # Extract equivalent von Mises stress
    stress_op = model.results.stress()
    stress_fc = stress_op.eqv().eval()

    # Get the first field from the container
    stress_field = stress_fc[0]

    # Display field information
    print(f"Stress field:")
    print(f"  Location: {stress_field.location}")
    print(f"  Number of entities: {stress_field.scoping.size}")
    print(f"  Unit: {stress_field.unit}")
    print(f"  Min value: {min(stress_field.data):.2f}")
    print(f"  Max value: {max(stress_field.data):.2f}")

Create Target Coordinates for Mapping
--------------------------------------

Now we define the coordinates where we want to map the results. We'll create a set of points along a line.

Define a Line of Points
^^^^^^^^^^^^^^^^^^^^^^^

Let's create a line of points through the model to extract stress values along a path.

.. jupyter-execute::

    # Get the bounding box of the mesh to define the path
    nodes_coords = mesh.nodes.coordinates_field

    # Get min and max coordinates
    all_x = [nodes_coords.data[i][0] for i in range(mesh.nodes.n_nodes)]
    all_y = [nodes_coords.data[i][1] for i in range(mesh.nodes.n_nodes)]
    all_z = [nodes_coords.data[i][2] for i in range(mesh.nodes.n_nodes)]

    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    min_z, max_z = min(all_z), max(all_z)

    print(f"Mesh bounding box:")
    print(f"  X: [{min_x:.6f}, {max_x:.6f}]")
    print(f"  Y: [{min_y:.6f}, {max_y:.6f}]")
    print(f"  Z: [{min_z:.6f}, {max_z:.6f}]")

    # Define a line of points along the Y-axis at the center
    center_x = (min_x + max_x) / 2.0
    center_z = (min_z + max_z) / 2.0

    # Create points along the Y direction
    n_points = 20
    coordinates = []
    for i in range(n_points):
        y_coord = min_y + (max_y - min_y) * i / (n_points - 1)
        coordinates.append([center_x, y_coord, center_z])

    print(f"\nCreated {len(coordinates)} points along a line")
    print(f"First point: {coordinates[0]}")
    print(f"Last point: {coordinates[-1]}")

Create a Field from Coordinates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to convert our coordinate list into a DPF |Field| object that can be used by the mapping operator.

.. jupyter-execute::

    # Create a 3D vector field to store coordinates
    coordinates_field = dpf.fields_factory.create_3d_vector_field(n_entities=len(coordinates))

    # Set the coordinate data
    coordinates_field.data = coordinates

    # Set scoping IDs for the points
    coordinates_field.scoping.ids = list(range(1, len(coordinates) + 1))

    # Display field information
    print(f"Coordinates field:")
    print(f"  Number of points: {coordinates_field.scoping.size}")
    print(f"  Components: {coordinates_field.component_count}")
    print(f"  First coordinate: {coordinates_field.data[0]}")

Map Results Using the Mapping Operator
---------------------------------------

Now we use the :class:`mapping operator <ansys.dpf.core.operators.mapping.on_coordinates>` to interpolate the stress results onto our custom coordinates.

Basic Mapping
^^^^^^^^^^^^^

Let's perform the basic mapping operation.

.. jupyter-execute::

    # Create the mapping operator
    mapping_op = ops.mapping.on_coordinates()

    # Connect inputs
    mapping_op.inputs.fields_container.connect(stress_fc)
    mapping_op.inputs.coordinates.connect(coordinates_field)
    mapping_op.inputs.mesh.connect(mesh)

    # Evaluate to get mapped results
    mapped_fc = mapping_op.outputs.fields_container()

    # Get the mapped field
    mapped_field = mapped_fc[0]

    # Display mapped field information
    print(f"Mapped stress field:")
    print(f"  Number of points: {mapped_field.scoping.size}")
    print(f"  Unit: {mapped_field.unit}")
    print(f"  Min value: {min(mapped_field.data):.2f}")
    print(f"  Max value: {max(mapped_field.data):.2f}")

The mapping operator has successfully interpolated stress values at each of our target coordinates by finding the containing element and using shape functions.

Mapping with Support Creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can also create a mesh support for the mapped results, which is useful for visualization.

.. jupyter-execute::

    # Create mapping operator with support creation
    mapping_with_support = ops.mapping.on_coordinates(
        fields_container=stress_fc,
        coordinates=coordinates_field,
        mesh=mesh,
        create_support=True
    )

    # Evaluate to get mapped results
    mapped_with_support_fc = mapping_with_support.eval()

    # Get the mapped field and its mesh support
    mapped_field_with_support = mapped_with_support_fc[0]

    # Check if the field has a meshed region support
    if mapped_field_with_support.meshed_region is not None:
        support_mesh = mapped_field_with_support.meshed_region
        print(f"Mapped field has mesh support:")
        print(f"  Number of nodes: {support_mesh.nodes.n_nodes}")
        print(f"  Number of elements: {support_mesh.elements.n_elements}")
    else:
        print("No mesh support created")

Analyze Mapped Results
-----------------------

Let's analyze the mapped stress values along the path.

Extract Data for Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^

We can extract the mapped data and corresponding coordinates for further analysis.

.. jupyter-execute::

    # Get mapped stress values
    mapped_stress_values = list(mapped_field.data)

    # Get the Y coordinates of the mapped points
    y_coordinates = [coordinates[i][1] for i in range(len(coordinates))]

    # Display some statistics
    print(f"Stress distribution along the path:")
    print(f"  Mean stress: {sum(mapped_stress_values) / len(mapped_stress_values):.2f} {mapped_field.unit}")
    print(f"  Min stress: {min(mapped_stress_values):.2f} {mapped_field.unit}")
    print(f"  Max stress: {max(mapped_stress_values):.2f} {mapped_field.unit}")

    # Find location of maximum stress
    max_stress_idx = mapped_stress_values.index(max(mapped_stress_values))
    print(f"\nMaximum stress location:")
    print(f"  Index: {max_stress_idx}")
    print(f"  Y-coordinate: {y_coordinates[max_stress_idx]:.6f}")
    print(f"  Stress value: {mapped_stress_values[max_stress_idx]:.2f} {mapped_field.unit}")

Advanced Mapping Options
-------------------------

The mapping operator provides several advanced options for controlling the mapping process.

Tolerance Control
^^^^^^^^^^^^^^^^^

The tolerance parameter controls the accuracy of the iterative algorithm used to locate coordinates inside the mesh.

.. jupyter-execute::

    # Create mapping operator with custom tolerance
    mapping_custom_tolerance = ops.mapping.on_coordinates(
        fields_container=stress_fc,
        coordinates=coordinates_field,
        mesh=mesh,
        tolerance=1e-6  # More precise than default (5e-5)
    )

    # Evaluate the mapping
    mapped_custom_tol_fc = mapping_custom_tolerance.eval()
    mapped_custom_tol_field = mapped_custom_tol_fc[0]

    print(f"Mapped with custom tolerance:")
    print(f"  Number of points: {mapped_custom_tol_field.scoping.size}")
    print(f"  Mean stress: {sum(mapped_custom_tol_field.data) / len(mapped_custom_tol_field.data):.2f} {mapped_custom_tol_field.unit}")

Mapping on Grid Points
^^^^^^^^^^^^^^^^^^^^^^^

We can also map results onto a 2D or 3D grid of points for creating custom visualizations.

.. jupyter-execute::

    # Create a 2D grid of points in the XY plane
    grid_size = 5
    grid_coordinates = []

    # Create grid within the bounding box
    for i in range(grid_size):
        for j in range(grid_size):
            x_coord = min_x + (max_x - min_x) * i / (grid_size - 1)
            y_coord = min_y + (max_y - min_y) * j / (grid_size - 1)
            z_coord = center_z
            grid_coordinates.append([x_coord, y_coord, z_coord])

    # Create field from grid coordinates
    grid_field = dpf.fields_factory.create_3d_vector_field(n_entities=len(grid_coordinates))
    grid_field.data = grid_coordinates
    grid_field.scoping.ids = list(range(1, len(grid_coordinates) + 1))

    # Map stress onto the grid
    grid_mapping = ops.mapping.on_coordinates(
        fields_container=stress_fc,
        coordinates=grid_field,
        mesh=mesh
    )

    grid_mapped_fc = grid_mapping.eval()
    grid_mapped_field = grid_mapped_fc[0]

    print(f"Mapped stress on {grid_size}x{grid_size} grid:")
    print(f"  Total grid points: {len(grid_coordinates)}")
    print(f"  Mapped points: {grid_mapped_field.scoping.size}")
    print(f"  Mean stress: {sum(grid_mapped_field.data) / len(grid_mapped_field.data):.2f} {grid_mapped_field.unit}")

Practical Applications
-----------------------

Let's explore some practical applications of coordinate mapping.

Extract Results at Specific Points of Interest
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can extract results at specific critical points in your model.

.. jupyter-execute::

    # Define specific points of interest
    critical_points = [
        [center_x, min_y + 0.25 * (max_y - min_y), center_z],  # Point at 25% height
        [center_x, min_y + 0.50 * (max_y - min_y), center_z],  # Point at 50% height
        [center_x, min_y + 0.75 * (max_y - min_y), center_z],  # Point at 75% height
    ]

    # Create field for critical points
    critical_points_field = dpf.fields_factory.create_3d_vector_field(n_entities=len(critical_points))
    critical_points_field.data = critical_points
    critical_points_field.scoping.ids = list(range(1, len(critical_points) + 1))

    # Map results to critical points
    critical_mapping = ops.mapping.on_coordinates(
        fields_container=stress_fc,
        coordinates=critical_points_field,
        mesh=mesh
    )

    critical_mapped_fc = critical_mapping.eval()
    critical_mapped_field = critical_mapped_fc[0]

    # Display results at critical points
    print("Stress at critical points:")
    for i, (point, stress) in enumerate(zip(critical_points, critical_mapped_field.data)):
        print(f"  Point {i+1} at Y={point[1]:.6f}: {stress:.2f} {critical_mapped_field.unit}")

Mapping Summary and Best Practices
-----------------------------------

Let's summarize the key concepts and best practices for using the mapping operator.

.. jupyter-execute::

    print("Mapping Operator Summary:")
    print("=" * 60)

    print("\nKey Inputs:")
    print("  - fields_container: Results to be mapped")
    print("  - coordinates: Target locations (Field with 3D coordinates)")
    print("  - mesh: Source mesh for interpolation")

    print("\nOptional Parameters:")
    print("  - create_support: Create mesh support for mapped results")
    print("  - tolerance: Accuracy of coordinate location (default: 5e-5)")
    print("  - use_quadratic_elements: Use quadratic interpolation for higher precision")

    print("\nCommon Use Cases:")
    print("  1. Path extraction - Results along lines or curves")
    print("  2. Point probing - Evaluate at specific locations")
    print("  3. Grid sampling - Create custom visualization grids")
    print("  4. Cross-section analysis - Results on planar cuts")

    print("\nBest Practices:")
    print("  - Ensure target coordinates are within the mesh bounds")
    print("  - Use create_support=True for visualization")
    print("  - Adjust tolerance for complex geometries")
    print("  - Consider using mapping_on_scoping for repeated operations")

    print(f"\nIn this tutorial:")
    print(f"  - Original mesh nodes: {mesh.nodes.n_nodes}")
    print(f"  - Mapped to {n_points} points along a path")
    print(f"  - Successfully interpolated stress values")
    print(f"  - Range: {min(mapped_stress_values):.2f} to {max(mapped_stress_values):.2f} {mapped_field.unit}")
