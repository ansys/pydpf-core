.. _ref_tutorials_collections:

===============
DPF Collections
===============

.. include:: ../../links_and_refs.rst

This tutorial shows how to create and work with some DPF collections: FieldsContainer, MeshesContainer and ScopingsContainer.

DPF collections are homogeneous groups of labeled raw data storage structures that allow you to organize and manipulate related data efficiently. Collections are essential for handling multiple time steps, frequency sets, or other labeled datasets in your analysis workflows.

:jupyter-download-script:`Download tutorial as Python script<collections>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<collections>`

Introduction to Collections
---------------------------

Collections in DPF serve as containers that group related objects with labels. The main collection types are:

- |FieldsContainer|: A collection of |Field| objects, typically representing results over multiple time steps or frequency sets
- |MeshesContainer|: A collection of |MeshedRegion| objects for different configurations or time steps  
- |ScopingsContainer|: A collection of |Scoping| objects for organizing entity selections

Each collection provides methods to:

- Add, retrieve, and iterate over contained objects
- Access objects by label (time, frequency, set ID, etc.)
- Perform operations across all contained objects

Set up the Analysis
-------------------

First, we import the required modules and load a transient analysis result file that contains multiple time steps.

.. jupyter-execute::

    # Import the ansys.dpf.core module
    import ansys.dpf.core as dpf
    
    # Import the examples module 
    from ansys.dpf.core import examples
    
    # Load a transient analysis with multiple time steps
    result_file_path = examples.find_msup_transient()
    
    # Create a DataSources object
    data_sources = dpf.DataSources(result_path=result_file_path)
    
    # Create a Model from the data sources
    model = dpf.Model(data_sources=data_sources)
    
    # Display basic model information
    print(f"Number of time steps: {len(model.metadata.time_freq_support.time_frequencies)}")
    print(f"Available results: {model.metadata.result_info.available_results}")

Working with FieldsContainer
-----------------------------

A |FieldsContainer| is the most commonly used collection in DPF. It stores multiple |Field| objects, each associated with a label such as time step or frequency.

Extract Results into a FieldsContainer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's extract displacement results for all time steps, which will automatically create a |FieldsContainer|.

.. jupyter-execute::

    # Get displacement results for all time steps
    displacement_fc = model.results.displacement.eval()
    
    # Display FieldsContainer information
    print(displacement_fc)

Access Individual Fields in the Container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can access individual fields by their label or index.

.. jupyter-execute::

    # Access field by index (first time step)
    first_field = displacement_fc[0]
    print(f"First field info:")
    print(f"  Location: {first_field.location}")
    print(f"  Number of entities: {first_field.scoping.size}")
    print(f"  Components: {first_field.component_count}")
    
    # Access field by label (specific time step)
    time_sets = list(displacement_fc.get_label_space(0).keys())
    if len(time_sets) > 1:
        second_time_field = displacement_fc.get_field({"time": time_sets[1]})
        print(f"\nSecond time step field:")
        print(f"  Time set: {time_sets[1]}")
        print(f"  Max displacement magnitude: {max(second_time_field.data):.6f}")

Create a Custom FieldsContainer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can create your own |FieldsContainer| and add fields with custom labels.

.. jupyter-execute::

    # Create an empty FieldsContainer
    custom_fc = dpf.FieldsContainer()
    
    # Set up labels for the container
    custom_fc.labels = ["time", "zone"]
    
    # Create sample fields for different time steps and zones  
    for time_step in [1, 2]:
        for zone in [1, 2]:
            # Create a simple field with sample data
            field = dpf.Field(location=dpf.locations.nodal, nature=dpf.natures.scalar)
            
            # Add some sample nodes and data
            field.scoping.ids = [1, 2, 3, 4, 5]
            field.data = [float(time_step * zone * i) for i in range(1, 6)]
            
            # Add field to container with labels
            custom_fc.add_field({"time": time_step, "zone": zone}, field)
    
    # Display the custom FieldsContainer
    print(custom_fc)

Working with ScopingsContainer
------------------------------

A |ScopingsContainer| holds multiple |Scoping| objects, which define sets of entity IDs (nodes, elements, etc.).

Create and Populate a ScopingsContainer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's create different node selections and organize them in a |ScopingsContainer|.

.. jupyter-execute::

    # Get the mesh from our model
    mesh = model.metadata.meshed_region
    
    # Create a ScopingsContainer
    scopings_container = dpf.ScopingsContainer()
    # Set labels for different selections
    scopings_container.labels = ["selection_type"]
    # Selection 1: First 10 nodes
    first_nodes = dpf.Scoping(location=dpf.locations.nodal)
    first_nodes.ids = list(range(1, 11))
    scopings_container.add_scoping(label_space={"selection_type": 0}, scoping=first_nodes)
    # Selection 2: Every 10th node (sample)
    all_node_ids = mesh.nodes.scoping.ids
    every_tenth = dpf.Scoping(location=dpf.locations.nodal)
    every_tenth.ids = all_node_ids[::10]  # Every 10th node
    scopings_container.add_scoping(label_space={"selection_type": 1}, scoping=every_tenth)
    # Selection 3: Last 10 nodes
    last_nodes = dpf.Scoping(location=dpf.locations.nodal)
    last_nodes.ids = all_node_ids[-10:]
    scopings_container.add_scoping(label_space={"selection_type": 2}, scoping=last_nodes)

    # Display ScopingsContainer information
    print(scopings_container)
    
    # Show details of each scoping
    for i, scoping in enumerate(scopings_container):
        label_space = scopings_container.get_label_space(i)
        print(f"  Scoping {i}: {label_space} - {scoping.size} entities")

Use ScopingsContainer with Operators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|ScopingsContainer| objects can be used with operators to apply operations to multiple selections.

.. jupyter-execute::

    # Create an operator to extract displacement on specific node sets
    displacement_op = dpf.operators.result.displacement()
    displacement_op.inputs.data_sources(data_sources)
    displacement_op.inputs.mesh_scoping(scopings_container)
    
    # Evaluate to get results for all scopings
    scoped_displacements = displacement_op.eval()
    
    print(f"Displacement results for different node selections:")
    print(f"  Result type: {type(scoped_displacements)}")
    print(f"  Number of result fields: {len(scoped_displacements)}")
    
    # Display information for each scoped result
    for i, field in enumerate(scoped_displacements):
        label_space = scoped_displacements.get_label_space(i)
        max_displacement = field.data.max()
        print(f"  Field {i}: {label_space} - {field.scoping.size} nodes, max displacement: {max_displacement:.6f}")

Working with MeshesContainer
----------------------------

A |MeshesContainer| stores multiple |MeshedRegion| objects. This is useful when working with different mesh configurations or time-dependent meshes.

Create a MeshesContainer
^^^^^^^^^^^^^^^^^^^^^^^^

Let's create a |MeshesContainer| with mesh data for different analysis configurations.

.. jupyter-execute::

    # Create a MeshesContainer
    meshes_container = dpf.MeshesContainer()

    # Set labels for different mesh configurations
    meshes_container.labels = ["variation"]

    # Get the original mesh
    original_mesh = model.metadata.meshed_region

    # Add original mesh
    meshes_container.add_mesh({"variation": 0}, original_mesh)

    # Create a modified mesh (example: subset of elements)
    # Get element scoping for first half of elements
    all_element_ids = original_mesh.elements.scoping.ids
    subset_element_ids = all_element_ids[:len(all_element_ids)//2]

    # Create element scoping for subset
    element_scoping = dpf.Scoping(location=dpf.locations.elemental)
    element_scoping.ids = subset_element_ids

    # Extract subset mesh using an operator
    mesh_extract_op = dpf.operators.mesh.from_scoping()
    mesh_extract_op.inputs.mesh(original_mesh)
    mesh_extract_op.inputs.scoping(element_scoping)
    subset_mesh = mesh_extract_op.eval()

    # Add subset mesh to container
    meshes_container.add_mesh({"variation": 1}, subset_mesh)

    # Display MeshesContainer information
    print(meshes_container)

Collection Operations and Iteration
------------------------------------

Collections support various operations for data manipulation and analysis.

Iterate Through Collections
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can iterate through collections using different methods.

.. jupyter-execute::

    # Iterate through FieldsContainer by index
    print("Iterating through displacement fields by index:")
    for i in range(min(3, len(displacement_fc))):  # Show first 3 fields
        field = displacement_fc[i]
        label_space = displacement_fc.get_label_space(i)
        max_value = field.data.max()
        print(f"  Field {i}: {label_space}, max value: {max_value:.6f}")
    
    print("\nIterating through ScopingsContainer:")
    for i, scoping in enumerate(scopings_container):
        label_space = scopings_container.get_label_space(i)
        print(f"  Scoping {i}: {label_space}, size: {scoping.size}")

Filter and Select from Collections  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can filter collections based on labels or criteria.

.. jupyter-execute::

    # Get specific fields from FieldsContainer by label criteria
    if len(displacement_fc) >= 2:
        # Get the second time step
        time_sets = list(displacement_fc.get_label_space(0).keys())
        if len(time_sets) > 1:
            specific_field = displacement_fc.get_field({"time": time_sets[1]})
            print(f"Retrieved field for time {time_sets[1]}:")
            print(f"  Components: {specific_field.component_count}")
            print(f"  Location: {specific_field.location}")
    
    # Get scoping by selection criteria
    first_ten_scoping = scopings_container.get_scoping({"selection_type": 0})
    print(f"\nRetrieved 'first_ten' scoping:")
    print(f"  Size: {first_ten_scoping.size}")
    print(f"  First 5 IDs: {first_ten_scoping.ids[:5]}")

Collection Summary and Best Practices
--------------------------------------

Let's summarize the key concepts and best practices for working with DPF collections.

.. jupyter-execute::

    print("DPF Collections Summary:")
    print("=" * 50)
    
    print(f"\n1. FieldsContainer:")
    print(f"   - Purpose: Store multiple Field objects with labels")
    print(f"   - Common use: Results over time steps, frequencies, or load cases")
    
    print(f"\n2. ScopingsContainer:")
    print(f"   - Purpose: Store multiple Scoping objects (entity selections)")
    print(f"   - Common use: Different node/element selections for analysis")
    
    print(f"\n3. MeshesContainer:")
    print(f"   - Purpose: Store multiple MeshedRegion objects")
    print(f"   - Common use: Different mesh configurations or time-dependent meshes")
    
    print(f"\nKey Benefits:")
    print(f"   - Efficient organization of related data")
    print(f"   - Label-based access for easy data retrieval")
    print(f"   - Integration with DPF operators for batch processing")
    print(f"   - Memory-efficient handling of large datasets")