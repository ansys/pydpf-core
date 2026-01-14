.. _ref_tutorials_mapping_prepare_workflow:

============================
RBF-based workflow mapping
============================

.. |prepare_mapping_workflow| replace:: :class:`prepare_mapping_workflow<ansys.dpf.core.operators.mapping.prepare_mapping_workflow>`
.. |Workflow| replace:: :class:`Workflow<ansys.dpf.core.workflow.Workflow>`
.. |Field| replace:: :class:`Field<ansys.dpf.core.field.Field>`
.. |MeshedRegion| replace:: :class:`MeshedRegion<ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Model| replace:: :class:`Model<ansys.dpf.core.model.Model>`
.. |fields_factory| replace:: :mod:`fields_factory<ansys.dpf.core.fields_factory>`

Generate a workflow for mapping results using RBF filters.

This tutorial demonstrates how to use the |prepare_mapping_workflow| operator to
generate a reusable workflow that maps results from one support to another using
Radial Basis Function (RBF) filters. This is particularly useful when you need to
transfer data between different mesh representations or interpolate results to a
different spatial support.

:jupyter-download-script:`Download tutorial as Python script<mapping_prepare_workflow>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<mapping_prepare_workflow>`

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

Define the input support
------------------------

Define the support from which you want to map results. This can be a |Field| or a |MeshedRegion|.

.. jupyter-execute::

    # Get the mesh as the input support
    input_mesh = model.metadata.meshed_region

    # Print input mesh information
    print("Input support (mesh):")
    print(input_mesh)

Define the output support
-------------------------

Define the target support where you want to map the results. Here we create a set
of target points.

.. jupyter-execute::

    # Define target points for the output support
    target_points = np.array([
        [0.01, 0.04, 0.01],
        [0.015, 0.045, 0.015],
        [0.02, 0.05, 0.02],
        [0.025, 0.055, 0.025]
    ])

    # Create a Field to represent the output support
    output_support_field = dpf.fields_factory.create_3d_vector_field(num_entities=len(target_points))
    output_support_field.data = target_points

    # Print the output support field
    print("\nOutput support (target coordinates):")
    print(output_support_field)

Prepare the mapping workflow
-----------------------------

Use the |prepare_mapping_workflow| operator to generate a workflow that can map
results from the input support to the output support using RBF filters.

.. jupyter-execute::

    # Define the filter radius for RBF interpolation
    # This controls the influence radius of each point
    filter_radius = 0.02

    # Create the prepare_mapping_workflow operator
    prepare_op = ops.mapping.prepare_mapping_workflow(
        input_support=input_mesh,
        output_support=output_support_field,
        filter_radius=filter_radius
    )

    # Evaluate to get the mapping workflow
    mapping_workflow = prepare_op.eval()

    # Print the workflow information
    print("Generated mapping workflow:")
    print(mapping_workflow)

Examine the generated workflow
------------------------------

The generated workflow contains operators that perform the RBF-based mapping.

.. jupyter-execute::

    # Get the operators in the workflow
    workflow_operators = mapping_workflow.operator_names

    # Print the operators
    print("Operators in the mapping workflow:")
    for i, op_name in enumerate(workflow_operators):
        print(f"  {i+1}. {op_name}")

Use the workflow to map results
--------------------------------

Apply the generated workflow to map actual field data.

.. jupyter-execute::

    # Get displacement results
    displacement_fc = model.results.displacement.eval()
    displacement_field = displacement_fc[0]

    # Print the input displacement field
    print("Input displacement field:")
    print(displacement_field)

.. jupyter-execute::

    # Connect the displacement field to the workflow
    # The workflow has inputs and outputs
    print("\nWorkflow inputs:")
    for input_name in mapping_workflow.input_names:
        print(f"  - {input_name}")

    # Connect the field to the workflow input
    mapping_workflow.connect_with(pin_in=0, inpt=displacement_field)

    # Execute the workflow
    mapped_displacement_field = mapping_workflow.get_output(pin=0, output_type=dpf.types.field)

    # Print the mapped field
    print("\nMapped displacement field:")
    print(mapped_displacement_field)

Compare input and output
-------------------------

Compare the sizes and values of the input and output fields.

.. jupyter-execute::

    # Compare field sizes
    print(f"Input field size: {len(displacement_field.data)}")
    print(f"Output field size: {len(mapped_displacement_field.data)}")

    # Print sample values
    print(f"\nSample input displacement (first 3 entities):")
    print(displacement_field.data[:3])

    print(f"\nSample output displacement (all entities):")
    print(mapped_displacement_field.data)

Use with influence box parameter
---------------------------------

The influence box parameter can further control the RBF filter behavior.

.. jupyter-execute::

    # Create a mapping workflow with influence box
    influence_box = 0.03

    prepare_op_with_box = ops.mapping.prepare_mapping_workflow(
        input_support=input_mesh,
        output_support=output_support_field,
        filter_radius=filter_radius,
        influence_box=influence_box
    )

    # Evaluate to get the workflow
    mapping_workflow_with_box = prepare_op_with_box.eval()

    # Print workflow information
    print("Mapping workflow with influence box:")
    print(mapping_workflow_with_box)

Map different result types
---------------------------

Reuse the same workflow to map different field types.

.. jupyter-execute::

    # Get stress results
    stress_fc = model.results.stress.eval()
    stress_field = stress_fc[0]

    # Use the original mapping workflow with stress
    mapping_workflow.connect_with(pin_in=0, inpt=stress_field)

    # Execute the workflow for stress
    mapped_stress_field = mapping_workflow.get_output(pin=0, output_type=dpf.types.field)

    # Print the mapped stress field
    print("Mapped stress field:")
    print(mapped_stress_field)

    # Print sample values
    print(f"\nSample mapped stress values:")
    print(mapped_stress_field.data[:2])

Use mesh as output support
---------------------------

You can also use a mesh as the output support for mesh-to-mesh mapping.

.. jupyter-execute::

    # Create a coarser output mesh or use an external mesh
    # For demonstration, we'll create a subset of the original mesh

    # Get a subset of elements for the output mesh
    element_scoping = dpf.Scoping(ids=list(range(1, 20)), location=dpf.locations.elemental)

    # Extract submesh
    submesh_op = ops.mesh.from_scoping(mesh=input_mesh, scoping=element_scoping)
    output_mesh = submesh_op.eval()

    # Print output mesh
    print("Output mesh (subset of input):")
    print(output_mesh)

.. jupyter-execute::

    # Create mapping workflow with mesh as output support
    prepare_mesh_op = ops.mapping.prepare_mapping_workflow(
        input_support=input_mesh,
        output_support=output_mesh,
        filter_radius=filter_radius
    )

    # Evaluate to get the workflow
    mesh_to_mesh_workflow = prepare_mesh_op.eval()

    # Print workflow
    print("\nMesh-to-mesh mapping workflow:")
    print(mesh_to_mesh_workflow)

.. jupyter-execute::

    # Use the mesh-to-mesh workflow
    mesh_to_mesh_workflow.connect_with(pin_in=0, inpt=displacement_field)

    # Execute the workflow
    mapped_to_mesh = mesh_to_mesh_workflow.get_output(pin=0, output_type=dpf.types.field)

    # Print the result
    print("Displacement mapped to output mesh:")
    print(mapped_to_mesh)

Adjust filter radius
--------------------

The filter radius parameter significantly affects the mapping quality and smoothness.

.. jupyter-execute::

    # Test different filter radii
    filter_radii = [0.01, 0.02, 0.04]

    for radius in filter_radii:
        # Create workflow with specific radius
        prep_op = ops.mapping.prepare_mapping_workflow(
            input_support=input_mesh,
            output_support=output_support_field,
            filter_radius=radius
        )

        workflow = prep_op.eval()

        # Map displacement
        workflow.connect_with(pin_in=0, inpt=displacement_field)
        result = workflow.get_output(pin=0, output_type=dpf.types.field)

        # Print results for comparison
        print(f"\nWith filter radius = {radius}:")
        print(f"  Mapped values range: [{result.min().data}, {result.max().data}]")

When to use this approach
--------------------------

Use the |prepare_mapping_workflow| operator when:

- You need to transfer data between different mesh representations
- You want to use RBF-based interpolation for smooth field mapping
- You need a reusable workflow for mapping multiple field types
- You are performing mesh-to-mesh data transfer
- You want more control over the interpolation via filter parameters
