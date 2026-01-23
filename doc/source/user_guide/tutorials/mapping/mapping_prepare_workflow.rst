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
generate a reusable workflow that maps results between non-conforming meshes using
Radial Basis Function (RBF) filters. This is particularly useful when you need to
transfer data between different mesh discretizations or when working with meshes
that have different topologies.

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

Define the target support where you want to map the results. For this tutorial, we'll
create a truly non-conforming mesh by extracting a subset of the original mesh and
perturbing the node coordinates to create a different mesh topology.

.. jupyter-execute::

    # Create a non-conforming mesh by extracting a subset and moving nodes
    
    # First, extract a coarser mesh by selecting every 3rd node
    original_node_ids = input_mesh.nodes.scoping.ids
    coarse_node_ids = original_node_ids[::3]
    
    # Create a scoping for the coarse nodes
    coarse_node_scoping = dpf.Scoping(ids=coarse_node_ids, location=dpf.locations.nodal)
    
    # Extract a submesh with these nodes
    mesh_extraction_op = ops.mesh.from_scoping(
        mesh=input_mesh,
        scoping=coarse_node_scoping,
        inclusive=1  # Include elements connected to selected nodes
    )
    subset_mesh = mesh_extraction_op.eval()
    
    # Now create a truly non-conforming mesh by perturbing the node coordinates
    # Get the coordinates field from the subset mesh
    coords_field = subset_mesh.nodes.coordinates_field
    
    # Get the coordinate data as a numpy array
    coords_data = coords_field.data.copy()
    
    # Add random perturbations to create a non-conforming mesh
    # Perturb by up to 5% of the model dimensions
    np.random.seed(42)  # For reproducibility
    perturbation_scale = 0.05 * np.max(np.ptp(coords_data, axis=0))
    perturbations = np.random.uniform(-perturbation_scale, perturbation_scale, coords_data.shape)
    perturbed_coords = coords_data + perturbations
    
    # Create a new field with perturbed coordinates
    from ansys.dpf.core import fields_factory
    perturbed_coords_field = fields_factory.field_from_array(perturbed_coords)
    perturbed_coords_field.scoping = coords_field.scoping
    
    # Create a new mesh with the perturbed coordinates
    output_mesh = subset_mesh.deep_copy()
    output_mesh.nodes.coordinates_field = perturbed_coords_field
    
    # Print the output mesh information
    print("Output support (non-conforming mesh with perturbed nodes):")
    print(output_mesh)
    print(f"\nInput mesh nodes: {input_mesh.nodes.n_nodes}")
    print(f"Output mesh nodes: {output_mesh.nodes.n_nodes}")
    print(f"Input mesh elements: {input_mesh.elements.n_elements}")
    print(f"Output mesh elements: {output_mesh.elements.n_elements}")
    print(f"Coordinate perturbation scale: {perturbation_scale:.6e}")

Prepare the mapping workflow
-----------------------------

Use the |prepare_mapping_workflow| operator to generate a workflow that can map
results from the input support to the output support using RBF filters. This allows
transferring field data between non-conforming meshes.

.. jupyter-execute::

    # Define the filter radius for RBF interpolation
    # This controls the influence radius of each point
    filter_radius = 0.02

    # Create the prepare_mapping_workflow operator
    prepare_op = ops.mapping.prepare_mapping_workflow(
        input_support=input_mesh,
        output_support=output_mesh,
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

    print("\nWorkflow outputs:")
    for output_name in mapping_workflow.output_names:
        print(f"  - {output_name}")

    # Get the first input and output names
    input_pin_name = mapping_workflow.input_names[0]
    output_pin_name = mapping_workflow.output_names[0]

    # Connect the field to the workflow input
    mapping_workflow.connect(pin_name=input_pin_name, inpt=displacement_field)

    # Execute the workflow
    mapped_displacement_field = mapping_workflow.get_output(pin_name=output_pin_name, output_type=dpf.types.field)

    # Print the mapped field
    print("\nMapped displacement field:")
    print(mapped_displacement_field)

Compare input and output
-------------------------

Compare the sizes and values of the input and output fields. Note that the output
field now has a size corresponding to the non-conforming output mesh.

.. jupyter-execute::

    # Compare field sizes
    print(f"Input field size: {len(displacement_field.data)}")
    print(f"Output field size: {len(mapped_displacement_field.data)}")
    print(f"Input mesh nodes: {input_mesh.nodes.n_nodes}")
    print(f"Output mesh nodes: {output_mesh.nodes.n_nodes}")

    # Print sample values
    print(f"\nSample input displacement (first 3 entities):")
    print(displacement_field.data[:3])

    print(f"\nSample output displacement (first 3 entities):")
    print(mapped_displacement_field.data[:3])

Use with influence box parameter
---------------------------------

The influence box parameter can further control the RBF filter behavior. This is
particularly useful for non-conforming mesh mapping to limit the search radius.

.. jupyter-execute::

    # Create a mapping workflow with influence box
    influence_box = 0.03

    prepare_op_with_box = ops.mapping.prepare_mapping_workflow(
        input_support=input_mesh,
        output_support=output_mesh,
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
    # Connect using the same input pin name
    mapping_workflow.connect(pin_name=input_pin_name, inpt=stress_field)

    # Execute the workflow for stress
    mapped_stress_field = mapping_workflow.get_output(pin_name=output_pin_name, output_type=dpf.types.field)

    # Print the mapped stress field
    print("Mapped stress field:")
    print(mapped_stress_field)

    # Print sample values
    print(f"\nSample mapped stress values:")
    print(mapped_stress_field.data[:2])

Use mesh as output support
---------------------------

You can use different mesh subsets or externally defined meshes as the output support.
Here we create an alternative output mesh with a different element selection.

.. jupyter-execute::

    # Create an alternative output mesh with different elements
    # Select elements from a different region of the mesh
    
    # Get a subset of elements for the alternative output mesh
    element_scoping = dpf.Scoping(ids=list(range(1, 50, 2)), location=dpf.locations.elemental)

    # Extract submesh
    submesh_op = ops.mesh.from_scoping(mesh=input_mesh, scoping=element_scoping)
    alternative_output_mesh = submesh_op.eval()

    # Print output mesh
    print("Alternative output mesh (different element selection):")
    print(alternative_output_mesh)
    print(f"Number of nodes: {alternative_output_mesh.nodes.n_nodes}")
    print(f"Number of elements: {alternative_output_mesh.elements.n_elements}")

.. jupyter-execute::

    # Create mapping workflow with alternative mesh as output support
    prepare_alt_mesh_op = ops.mapping.prepare_mapping_workflow(
        input_support=input_mesh,
        output_support=alternative_output_mesh,
        filter_radius=filter_radius
    )

    # Evaluate to get the workflow
    alt_mesh_to_mesh_workflow = prepare_alt_mesh_op.eval()

    # Print workflow
    print("\nAlternative mesh-to-mesh mapping workflow:")
    print(alt_mesh_to_mesh_workflow)

.. jupyter-execute::

    # Use the alternative mesh-to-mesh workflow
    # Get the input/output pin names from the workflow
    alt_mesh_input_pin = alt_mesh_to_mesh_workflow.input_names[0]
    alt_mesh_output_pin = alt_mesh_to_mesh_workflow.output_names[0]

    alt_mesh_to_mesh_workflow.connect(pin_name=alt_mesh_input_pin, inpt=displacement_field)

    # Execute the workflow
    mapped_to_alt_mesh = alt_mesh_to_mesh_workflow.get_output(pin_name=alt_mesh_output_pin, output_type=dpf.types.field)

    # Print the result
    print("Displacement mapped to alternative output mesh:")
    print(mapped_to_alt_mesh)
    print(f"\nMapped field size: {len(mapped_to_alt_mesh.data)}")
    print(f"Target mesh nodes: {alternative_output_mesh.nodes.n_nodes}")

Adjust filter radius
--------------------

The filter radius parameter significantly affects the mapping quality and smoothness
when transferring data between non-conforming meshes. A larger radius provides smoother
interpolation but may lose fine details.

.. jupyter-execute::

    # Test different filter radii
    filter_radii = [0.01, 0.02, 0.04]

    for radius in filter_radii:
        # Create workflow with specific radius
        prep_op = ops.mapping.prepare_mapping_workflow(
            input_support=input_mesh,
            output_support=output_mesh,
            filter_radius=radius
        )

        workflow = prep_op.eval()
        
        # Get the input and output pin names
        wf_input_pin = workflow.input_names[0]
        wf_output_pin = workflow.output_names[0]

        # Map displacement
        workflow.connect(pin_name=wf_input_pin, inpt=displacement_field)
        result = workflow.get_output(pin_name=wf_output_pin, output_type=dpf.types.field)

        # Print results for comparison
        print(f"\nWith filter radius = {radius}:")
        print(f"  Mapped values range: [{result.min().data}, {result.max().data}]")
        print(f"  Mean displacement magnitude: {np.mean(np.linalg.norm(result.data, axis=1)):.6e}")

When to use this approach
--------------------------

Use the |prepare_mapping_workflow| operator when:

- You need to transfer data between different mesh representations
- You want to use RBF-based interpolation for smooth field mapping
- You need a reusable workflow for mapping multiple field types
- You are performing mesh-to-mesh data transfer
- You want more control over the interpolation via filter parameters
