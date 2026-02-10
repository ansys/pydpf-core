.. _ref_tutorials_export_to_vtu:

====================================
Export simulation data to VTU format
====================================

:bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA` :bdg-fluent:`FLUENT` :bdg-cfx:`CFX`

.. include:: ../../../links_and_refs.rst
.. |migrate_to_vtu| replace:: :class:`migrate_to_vtu <ansys.dpf.core.operators.serialization.migrate_to_vtu.migrate_to_vtu>`
.. |DataSources| replace:: :class:`DataSources <ansys.dpf.core.data_sources.DataSources>`
.. |Scoping| replace:: :class:`Scoping <ansys.dpf.core.scoping.Scoping>`

Export simulation data to [VTU format](https://docs.vtk.org/en/latest/vtk_file_formats/vtkxml_file_format.html#unstructuredgrid) for visualization and analysis in
VTK-compatible tools like ParaView.

VTU (VTK Unstructured Grid) is the most common VTK file format for unstructured
mesh data and field results. It's an XML-based format that stores:

- Mesh geometry (nodes and element connectivity)
- Field data (displacement, stress, temperature, etc.)
- Time series information
- Metadata and units

By exporting to VTU, you can leverage the powerful visualization capabilities of
ParaView, VisIt, or any VTK-based application.

The |migrate_to_vtu| operator provides a streamlined workflow to export complete
simulation results to VTU format directly from result files. It automatically
handles mesh conversion, field mapping, and time series organization.

.. note::

    **When to use this operator:**

    - Use |migrate_to_vtu| for quick export of entire result files (this tutorial)
    - Use ``vtu_export`` when working with processed DPF objects (see :ref:`ref_tutorials_export_vtu_with_dpf_objects`)

:jupyter-download-script:`Download tutorial as Python script<export_to_vtu>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<export_to_vtu>`

Import required modules
-----------------------

First, import the required modules and set up the example file path.

.. jupyter-execute::

    # Import the ``ansys.dpf.core`` module
    from ansys.dpf import core as dpf
    # Import the examples module
    from ansys.dpf.core import examples
    # Import the operators module
    from ansys.dpf.core import operators as ops
    # Import os for directory creation
    import os

Basic VTU export
----------------

The simplest way to export simulation data is to provide a |DataSources| object
and an output directory. The operator will export all available results for all
time steps.

.. jupyter-execute::

    # Download an example result file
    result_file = examples.download_crankshaft()

    # Create a DataSources object
    data_sources = dpf.DataSources(result_file)

    # Create output directory
    output_dir = "./crankshaft_export"
    os.makedirs(output_dir, exist_ok=True)

    # Create the migrate_to_vtu operator
    migrate_op = ops.serialization.migrate_to_vtu(
        data_sources=data_sources,
        directory=output_dir
    )

    # Execute the export
    output_paths = migrate_op.eval()

    # Display information about exported files
    print(f"Number of VTU files exported: {output_paths.num_paths()}")
    print("\nExported files:")
    for path in output_paths.result_file_paths():
        print(f"  {path}")

Export specific time steps
---------------------------

You can filter which time steps to export by providing a time scoping. This is
useful when you only need specific time points from a transient analysis.

.. jupyter-execute::

    # Create output directory for filtered export
    output_dir_filtered = "./crankshaft_export_filtered"
    os.makedirs(output_dir_filtered, exist_ok=True)

    # Create a time scoping for specific time steps
    # Export only the first time step
    time_scoping = dpf.Scoping(location=dpf.locations.time_freq)
    time_scoping.ids = [1]

    # Create the migrate_to_vtu operator with time filtering
    migrate_op_filtered = ops.serialization.migrate_to_vtu(
        data_sources=data_sources,
        time_scoping=time_scoping,
        directory=output_dir_filtered,
        base_name="crankshaft_t1"
    )

    # Execute the export
    output_paths_filtered = migrate_op_filtered.eval()

    # Display information
    print(f"Exported {output_paths_filtered.num_paths()} file(s) for time step 1")

Customize output file naming
-----------------------------

The ``base_name`` parameter allows you to specify a custom prefix for the
exported VTU files. This is helpful when organizing multiple exports or when
you want meaningful file names.

.. jupyter-execute::

    # Create output directory with custom naming
    output_dir_custom = "./crankshaft_custom_name"
    os.makedirs(output_dir_custom, exist_ok=True)

    # Create the operator with custom base name
    migrate_op_custom = ops.serialization.migrate_to_vtu(
        data_sources=data_sources,
        time_scoping=dpf.Scoping(location=dpf.locations.time_freq, ids=[1, 2, 3]),  # Export first three time steps
        directory=output_dir_custom,
        base_name="my_simulation_results"
    )

    # Execute the export
    output_paths_custom = migrate_op_custom.eval()

    # Display the custom file names
    print("Exported files with custom naming:")
    for path in output_paths_custom.result_file_paths():
        print(f"  {os.path.basename(path)}")

Control output format
---------------------

The ``write_mode`` parameter controls how the VTU data is written. Different modes
provide trade-offs between file size, precision, and readability.

Available write modes:

- ``rawbinarycompressed`` (default): Best compression, smallest file size
- ``rawbinary``: Binary format without compression
- ``base64appended``: Base64-encoded binary data appended to XML
- ``base64inline``: Base64-encoded binary data inline with XML
- ``ascii``: Human-readable text format (useful for debugging, but large files)

.. jupyter-execute::

    # Create output directory for ASCII export
    output_dir_ascii = "./crankshaft_ascii"
    os.makedirs(output_dir_ascii, exist_ok=True)

    # Export in ASCII mode for debugging
    migrate_op_ascii = ops.serialization.migrate_to_vtu(
        data_sources=data_sources,
        time_scoping=[1],
        directory=output_dir_ascii,
        base_name="crankshaft_ascii",
        write_mode="ascii"
    )

    # Execute the export
    output_paths_ascii = migrate_op_ascii.eval()

    # Compare file sizes
    binary_file = output_paths_filtered.result_file_paths()[0]
    ascii_file = output_paths_ascii.result_file_paths()[0]

    print(f"Binary file size: {os.path.getsize(binary_file) / 1024:.2f} KB")
    print(f"ASCII file size: {os.path.getsize(ascii_file) / 1024:.2f} KB")

Complete workflow example
-------------------------

Here's a complete example that demonstrates a typical workflow for exporting
simulation results to VTU format for visualization in ParaView.

.. tab-set::

    .. tab-item:: MAPDL

        .. jupyter-execute::

            # Define the output directory
            mapdl_output_dir = "./mapdl_vtu_export"
            os.makedirs(mapdl_output_dir, exist_ok=True)

            # Load a MAPDL result file
            mapdl_result = examples.find_static_rst()
            mapdl_ds = dpf.DataSources(mapdl_result)

            # Get available time steps from the result
            time_freq_support = dpf.operators.metadata.time_freq_support_provider(
                data_sources=mapdl_ds
            ).eval()

            # Display available time steps
            print(f"Available time steps: {time_freq_support.time_frequencies.data}")

            # Export all time steps with optimized compression
            mapdl_migrate = ops.serialization.migrate_to_vtu(
                data_sources=mapdl_ds,
                directory=mapdl_output_dir,
                base_name="static_analysis",
                write_mode="rawbinarycompressed"
            )

            # Execute the export
            mapdl_output = mapdl_migrate.eval()

            # Display summary
            print(f"\nExported {mapdl_output.num_paths()} VTU file(s)")
            print(f"Output directory: {mapdl_output_dir}")
            print("\nTo visualize in ParaView:")
            print(f"  1. Open ParaView")
            print(f"  2. File -> Open -> Navigate to {mapdl_output_dir}")
            print(f"  3. Select the .vtu files and click 'Apply'")

    .. tab-item:: LS-DYNA

        .. jupyter-execute::

            # Define the output directory
            dyna_output_dir = "./lsdyna_vtu_export"
            os.makedirs(dyna_output_dir, exist_ok=True)

            # Load an LS-DYNA result file
            dyna_result = examples.download_d3plot_beam()
            dyna_ds = dpf.DataSources(dyna_result)

            # Export with custom configuration
            dyna_migrate = ops.serialization.migrate_to_vtu(
                data_sources=dyna_ds,
                directory=dyna_output_dir,
                base_name="beam_analysis",
                write_mode="rawbinarycompressed"
            )

            # Execute the export
            dyna_output = dyna_migrate.eval()

            # Display summary
            print(f"Exported {dyna_output.num_paths()} VTU file(s)")
            print(f"Output directory: {dyna_output_dir}")

    .. tab-item:: Fluent

        .. jupyter-execute::

            # Define the output directory
            fluent_output_dir = "./fluent_vtu_export"
            os.makedirs(fluent_output_dir, exist_ok=True)

            # Load a Fluent result file
            fluent_result = examples.download_fluent_axial_comp()
            fluent_ds = dpf.DataSources(fluent_result["cas"])
            fluent_ds.add_file_path(fluent_result["dat"])

            # Export with custom configuration
            fluent_migrate = ops.serialization.migrate_to_vtu(
                data_sources=fluent_ds,
                directory=fluent_output_dir,
                base_name="axial_comp",
                write_mode="rawbinarycompressed"
            )

            # Execute the export
            fluent_output = fluent_migrate.eval()

            # Display summary
            print(f"Exported {fluent_output.num_paths()} VTU file(s)")
            print(f"Output directory: {fluent_output_dir}")

Export selected results
-----------------------

By default, the |migrate_to_vtu| operator exports all available results from the
simulation file. If you only need specific results (for example, only displacement
and stress), you can specify which results to export using the ``result1`` and
``result2`` input pins. For additional results beyond the first two, use the
``Operator.connect()`` method with pin numbers starting at 30.

Discover available results
~~~~~~~~~~~~~~~~~~~~~~~~~~

Before exporting specific results, you can query the result file to see what
results are available and their corresponding operator names.

.. jupyter-execute::

    # Get the result information from the model
    result_info = model.metadata.result_info

    # Display all available results and the corresponding operator names
    for result in result_info.available_results:
        # Get the operator name for this result
        operator_name = result.operator_name
        # Get the result name (user-friendly name)
        result_name = result.name
        # Get number of components
        n_components = result.n_components

        print(f"{result_name:<30} {operator_name:<20} {n_components}")

.. note::

    The result names correspond to DPF operator names. Common result names include:

    - ``U`` or ``displacement`` for displacement
    - ``S`` or ``stress`` for stress
    - ``EPEL`` for elastic strain
    - ``TEMP`` for temperature
    - ``V`` or ``velocity`` for velocity

    Use the operator name when specifying which results to export.

Export specific results
~~~~~~~~~~~~~~~~~~~~~~~

Now that you know the available results and their operator names, you can
select specific results to export.

.. jupyter-execute::

    # Create output directory for selective export
    output_dir_selective = "./crankshaft_selective"
    os.makedirs(output_dir_selective, exist_ok=True)

    # Create the operator
    migrate_op_selective = ops.serialization.migrate_to_vtu(
        data_sources=data_sources,
        time_scoping=[1],
        directory=output_dir_selective,
        base_name="selected_results"
    )

    # Connect specific results using the result pins
    # Export displacement (U) and stress (S)
    migrate_op_selective.inputs.result1.connect("U")
    migrate_op_selective.inputs.result2.connect("S")
    # Connect additional results using the Operator.connect method (results start at pin 30)
    # Export velocity along X axis (VX) as an additional result
    migrate_op_selective.connect(pin=32, inpt="VX")
    # Execute the export
    output_paths_selective = migrate_op_selective.eval()

    print(f"Exported {output_paths_selective.num_paths()} file(s) with selected results")
    print("Included results: Displacement (U), Stress (S), and Velocity X (VX)")

Summary
-------

This tutorial demonstrated how to:

- Export all simulation results to VTU format using the |migrate_to_vtu| operator
- Filter exports to specific time steps using time scoping
- Customize output file naming with the ``base_name`` parameter
- Control file format and compression with the ``write_mode`` parameter
- Export only selected result types for focused analysis

The VTU export capability enables seamless integration with visualization tools like
ParaView, allowing you to leverage advanced post-processing features beyond what's
available in DPF alone.

.. tip::

    For best results when working with ParaView:

    - Use ``rawbinarycompressed`` mode for production exports (smallest files)
    - Use ``ascii`` mode only for debugging or when file size isn't a concern
    - Export time series data to create animations in ParaView
    - Organize exports into separate directories for different analyses
