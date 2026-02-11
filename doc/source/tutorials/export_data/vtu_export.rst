.. _ref_tutorials_vtu_export:

============================
Export VTU using DPF objects
============================

.. include:: ../../../links_and_refs.rst
.. |vtu_export| replace:: :class:`vtu_export <ansys.dpf.core.operators.serialization.vtu_export.vtu_export>`
.. |MeshedRegion| replace:: :class:`MeshedRegion <ansys.dpf.core.meshed_region.MeshedRegion>`
.. |Field| replace:: :class:`Field <ansys.dpf.core.field.Field>`
.. |FieldsContainer| replace:: :class:`FieldsContainer <ansys.dpf.core.fields_container.FieldsContainer>`

Export DPF data objects (mesh and fields) directly to VTU format using the
|vtu_export| operator.

The |vtu_export| operator provides fine-grained control over VTU export by working
directly with DPF objects rather than result files. This approach is ideal when you:

- Have already processed or modified data in DPF (filtered, averaged, transformed)
- Want to export custom fields created through operator workflows
- Need to combine data from multiple sources
- Require precise control over which mesh and fields to export
- Are working with data that doesn't come from simulation files

.. note::

    **When to use which operator:**

    - Use |migrate_to_vtu| for quick export of entire result files (see :ref:`ref_tutorials_export_to_vtu`)
    - Use |vtu_export| when working with processed DPF objects or custom workflows

:jupyter-download-script:`Download tutorial as Python script<export_vtu_with_dpf_objects>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<export_vtu_with_dpf_objects>`

Import required modules
-----------------------

First, import the required modules and set up the example data.

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module
    from ansys.dpf import core as dpf
    # Import the examples module
    from ansys.dpf.core import examples
    # Import the operators module
    from ansys.dpf.core import operators as ops
    # Import os for directory creation
    import os

Basic VTU export with DPF objects
----------------------------------

Export a mesh and field data that you've already loaded or processed in DPF.

.. jupyter-execute::

    # Load result file and create a model
    result_file = examples.find_static_rst()
    model = dpf.Model(result_file)

    # Get the mesh
    mesh = model.metadata.meshed_region

    # Get displacement results as a FieldsContainer
    displacement_fc = model.results.displacement.on_all_time_freqs.eval()

    # Create output directory
    output_dir = "./dpf_objects_export"
    os.makedirs(output_dir, exist_ok=True)

    # Create the vtu_export operator
    export_op = ops.serialization.vtu_export(
        directory=output_dir,
        mesh=mesh,
        fields1=displacement_fc,
        base_name="displacement_results"
    )

    # Execute the export
    output_paths = export_op.eval()

    # Display information
    print(f"Exported {len(output_paths.result_files)} VTU file(s)")
    for path in output_paths.result_files[:3]:  # Show first 3
        print(f"  {path}")

Export multiple field types
----------------------------

Export multiple different field types (displacement, stress, temperature, etc.)
in a single VTU file.

.. jupyter-execute::

    # Create output directory
    output_dir_multi = "./multi_field_export"
    os.makedirs(output_dir_multi, exist_ok=True)

    # Get different result types
    displacement = model.results.displacement.on_all_time_freqs.eval()
    stress = model.results.stress.on_all_time_freqs.eval()

    # Create the vtu_export operator with multiple fields
    export_multi = ops.serialization.vtu_export(
        directory=output_dir_multi,
        mesh=mesh,
        fields1=displacement,
        fields2=stress,
        base_name="multi_field_results"
    )

    # Execute the export
    output_multi = export_multi.eval()

    print(f"Exported {len(output_multi.result_files)} VTU file(s) with displacement and stress")

Export processed data
---------------------

Export data that has been processed through DPF operators, such as averaging,
filtering, or custom transformations.

.. jupyter-execute::

    # Create output directory
    output_dir_processed = "./processed_export"
    os.makedirs(output_dir_processed, exist_ok=True)

    # Get stress results
    stress_fc = model.results.stress.on_all_time_freqs.eval()

    # Process the data - compute Von Mises equivalent stress
    von_mises_op = ops.invariant.von_mises_eqv_fc(fields_container=stress_fc)
    von_mises_fc = von_mises_op.eval()

    # Export the processed result
    export_processed = ops.serialization.vtu_export(
        directory=output_dir_processed,
        mesh=mesh,
        fields1=von_mises_fc,
        base_name="von_mises_stress"
    )

    output_processed = export_processed.eval()

    print(f"Exported processed Von Mises stress to {len(output_processed.result_files)} VTU file(s)")

Export a single time step
--------------------------

Export only a specific time step by working with individual |Field| objects
instead of |FieldsContainer| objects.

.. jupyter-execute::

    # Create output directory
    output_dir_single = "./single_timestep_export"
    os.makedirs(output_dir_single, exist_ok=True)

    # Get displacement at a specific time step
    time_scoping = dpf.Scoping()
    time_scoping.ids = [1]

    displacement_single = model.results.displacement.on_time_scoping(time_scoping).eval()

    # Get the first field from the container
    disp_field = displacement_single[0]

    # Export the single field
    export_single = ops.serialization.vtu_export(
        directory=output_dir_single,
        mesh=mesh,
        fields1=disp_field,
        base_name="displacement_timestep_1"
    )

    output_single = export_single.eval()

    print(f"Exported single time step to {len(output_single.result_files)} VTU file(s)")

Export with property fields
----------------------------

Include mesh property fields (element type, material ID, etc.) in the export.

.. jupyter-execute::

    # Create output directory
    output_dir_props = "./property_export"
    os.makedirs(output_dir_props, exist_ok=True)

    # Get material property field from the mesh
    mat_prop = mesh.property_field("mat")

    # Get displacement results
    displacement = model.results.displacement.on_all_time_freqs.eval()

    # Export with property field
    export_props = ops.serialization.vtu_export(
        directory=output_dir_props,
        mesh=mesh,
        fields1=displacement,
        fields2=mat_prop,
        base_name="results_with_material"
    )

    output_props = export_props.eval()

    print(f"Exported results with material properties to {len(output_props.result_files)} VTU file(s)")

Control output format
---------------------

Choose different VTU write modes for your specific needs.

.. jupyter-execute::

    # Create output directory
    output_dir_ascii = "./ascii_export"
    os.makedirs(output_dir_ascii, exist_ok=True)

    # Get a single field for comparison
    disp_field = displacement_fc[0]

    # Export in ASCII format (human-readable, larger file size)
    export_ascii = ops.serialization.vtu_export(
        directory=output_dir_ascii,
        mesh=mesh,
        fields1=disp_field,
        base_name="displacement_ascii",
        write_mode="ascii"
    )

    output_ascii = export_ascii.eval()

    # Export in compressed binary format (default, smallest file size)
    export_binary = ops.serialization.vtu_export(
        directory=output_dir_ascii,
        mesh=mesh,
        fields1=disp_field,
        base_name="displacement_binary",
        write_mode="rawbinarycompressed"
    )

    output_binary = export_binary.eval()

    # Compare file sizes
    ascii_file = output_ascii.result_files[0]
    binary_file = output_binary.result_files[0]

    print(f"ASCII file size: {os.path.getsize(ascii_file) / 1024:.2f} KB")
    print(f"Compressed binary file size: {os.path.getsize(binary_file) / 1024:.2f} KB")

Export point cloud data
-----------------------

Export mesh nodes as a point cloud without element connectivity.

.. jupyter-execute::

    # Create output directory
    output_dir_cloud = "./point_cloud_export"
    os.makedirs(output_dir_cloud, exist_ok=True)

    # Get nodal displacement field
    disp_field = displacement_fc[0]

    # Export as point cloud
    export_cloud = ops.serialization.vtu_export(
        directory=output_dir_cloud,
        mesh=mesh,
        fields1=disp_field,
        base_name="displacement_points",
        as_point_cloud=True
    )

    output_cloud = export_cloud.eval()

    print(f"Exported point cloud to {len(output_cloud.result_files)} VTU file")
    print("Note: File contains only point data without element connectivity")

Working with custom data
------------------------

Create and export completely custom field data.

.. jupyter-execute::

    # Create output directory
    output_dir_custom = "./custom_data_export"
    os.makedirs(output_dir_custom, exist_ok=True)

    # Create a custom scalar field
    custom_field = dpf.Field(location=dpf.locations.nodal, nature=dpf.natures.scalar)
    custom_field.scoping = mesh.nodes.scoping

    # Fill with custom data (example: distance from origin)
    import numpy as np
    coords = mesh.nodes.coordinates_field.data
    distances = np.sqrt(np.sum(coords**2, axis=1))
    custom_field.data = distances

    # Set a name for the field
    custom_field.name = "distance_from_origin"

    # Export the custom field
    export_custom = ops.serialization.vtu_export(
        directory=output_dir_custom,
        mesh=mesh,
        fields1=custom_field,
        base_name="custom_distance_field"
    )

    output_custom = export_custom.eval()

    print(f"Exported custom field to {len(output_custom.result_files)} VTU file")

Summary
-------

This tutorial demonstrated how to use the |vtu_export| operator to:

- Export DPF objects (|MeshedRegion| and |Field|/|FieldsContainer|) directly to VTU format
- Export multiple field types in a single VTU file
- Export processed or transformed data from operator workflows
- Export specific time steps or single fields
- Include mesh property fields in the export
- Control output format (ASCII, binary, compressed)
- Export point cloud data without element connectivity
- Create and export completely custom field data

**Key differences from migrate_to_vtu:**

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Aspect
     - migrate_to_vtu
     - vtu_export
   * - **Input**
     - Result file (DataSources)
     - DPF objects (MeshedRegion, Fields)
   * - **Use case**
     - Quick export of entire result files
     - Export processed/custom data
   * - **Control**
     - Limited (exports all available results)
     - Full control over mesh and fields
   * - **Workflow**
     - File-based, automatic
     - Object-based, manual

.. tip::

    **Choose the right operator:**

    - Use **migrate_to_vtu** when you want to quickly export all results from a simulation file
    - Use **vtu_export** when you need control over what gets exported or are working with processed data
