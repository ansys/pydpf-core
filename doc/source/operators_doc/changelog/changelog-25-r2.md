# Changelog
## Table of Contents
### Features categories
  * [Framework](#features_framework)
  * [HGP](#features_hgp)
  * [MAPDL](#features_mapdl)
  * [LSDYNA](#features_lsdyna)
  * [Math](#features_math)
  * [HDF5](#features_hdf5)
  * [Compression](#features_compression)
  * [Documentation](#features_documentation)
  * [Motion](#features_motion)
  * [CGNS](#features_cgns)

### Changes categories
  * [Framework](#changes_framework)
  * [HGP](#changes_hgp)
  * [MAPDL](#changes_mapdl)
  * [CFF](#changes_cff)
  * [LSDYNA](#changes_lsdyna)
  * [HDF5](#changes_hdf5)
  * [Math](#changes_math)
  * [Engineering Data](#changes_engineering_data)
  
### Fixes categories
  * [Framework](#fixes_framework)
  * [HGP](#fixes_hgp)
  * [MAPDL](#fixes_mapdl)
  * [CFF](#fixes_cff)
  * [LSDYNA](#fixes_lsdyna)
  * [Math](#fixes_math)
  * [HDF5](#fixes_hdf5)
  * [VTK](#fixes_vtk)

### Performance Improvements categories
  * [Framework](#performance_framework)
  * [HGP](#performance_hgp)
  * [MAPDL](#performance_mapdl)
  * [Compression](#performance_compression)

## Features

### <a id="features_framework"></a> Framework

###### <a id="source_operator_allow_to_return_all_timesfreq_fields"></a> Source operator: allow to return all times/freq fields


Add support of pin "time_scoping" with int value == -1 in source operators. When -1 is used, results for all times or frequencies will be returned.


###### <a id="improve_custom_source_op_to_support_all_providers_and_scripting_names"></a> Improve "custom" source op to support all providers and scripting names


- Rename "custom" operator to "result_provider"
- Add support of scripting name to request a specific result in "result_provider".


###### <a id="allow_normals_provider_to_compute_face_normals_when_no_elements"></a> Allow normals provider to compute face normals when no elements



###### <a id="allow_dpf_to_operate_without_context"></a> Allow DPF to operate without context


When initializing DPF, you can use a Context using `userDefinedContext` and an empty xml path. In that case, DPF will not load any plugin.


###### <a id="add_changelog_to_dpf"></a> Add Changelog to DPF

###### <a id="support_getting_the_field_of_a_fieldscontainer_with_fieldscontainergetattribute"></a> Support getting the field of a fieldscontainer with fieldscontainer::get_attribute

###### <a id="enabled_dimension_less_units_with_symbol"></a> Enabled dimension less units with symbol

###### <a id="modify_normal_and_shear_strain_calculation_when_cartesian_coordinate_system_is_selected"></a> Modify normal and shear strain calculation when cartesian coordinate system is selected

###### <a id="add_operator_versions"></a> Add Operator versions

###### <a id="handle_temperaturedifference_and_improve_unit_conversion_handling"></a> Handle TemperatureDifference and Improve unit conversion handling

###### <a id="add_pin_alias"></a> Add pin alias

###### <a id="add_readcyclic_pin_to_equivalent_mass_operator_specification"></a> Add read_cyclic pin to equivalent mass operator specification

###### <a id="create_comparison_operators_for_types_property__meshes_containers__generic_data_containers"></a> Create comparison operators for types, property & meshes containers & generic data containers.

###### <a id="display_an_explicit_error_message_when_the_ansysdpfacceptla_is_not_set_to_y_in_the_standalone"></a> Display an explicit error message when the ANSYS_DPF_ACCEPT_LA is not set to Y in the standalone.

###### <a id="creation_of_nodal_to_elemental_nodal_averaging_operator"></a> Creation of nodal to elemental nodal averaging operator.

###### <a id="add_operatorid_operator"></a> Add operator_id operator

###### <a id="add_option_to_serialize_in_a_binary_format"></a> Add option to serialize in a binary format

### <a id="features_hgp"></a> HGP

###### <a id="add_shell_layers_pin_to_hgp"></a> Add shell layers pin to HgP

###### <a id="workflow_getoutput_datatree"></a> Workflow getOutput DataTree

###### <a id="add_magneticpotential_as_an_available_homogeneity"></a> Add MagneticPotential as an available homogeneity

###### <a id="allow_to_create_a_dpfvector_for_any_type"></a> Allow to create a DpfVector for any type

### <a id="features_mapdl"></a> MAPDL

###### <a id="add_number_of_threads_control_to_mapdlrun_with_a_new_pin"></a> Add number of threads control to mapdl::run with a new pin

###### <a id="document_current_density_quirks"></a> Document current density quirks

###### <a id="support_for_solid225_elements"></a> Support for SOLID225 elements

###### <a id="support_contact_results_for_econta177_and_econta172_elements"></a> Support contact results for eCONTA177 and eCONTA172 elements

###### <a id="new_operator_for_psd_fsum"></a> New operator for PSD FSUM

###### <a id="handle_prets179_elements"></a> Handle PRETS179 elements

###### <a id="allowing_to_read_the_element_state_variable_record_esv"></a> Allowing to read the element state variable record (ESV)

###### <a id="elementtypesprovider_to_output_additional_data"></a> Element_types_provider to output additional data.

###### <a id="add_operators_to_read_magnetic_results"></a> Add operators to read magnetic results

###### <a id="shell93_enf__addition_of_composite_files"></a> SHELL93 ENF + Addition of composite files

###### <a id="make_spectrumdata_a_source_operator_and_expose_prs_reader"></a> Make spectrum_data a source operator and expose .prs reader

### <a id="features_lsdyna"></a> LSDYNA

###### <a id="support_get_shell_ipts_on_all_layers"></a> Support extraction of results on all integration points of shells with more than 3 through-thickness integration points

###### <a id="support_viscosity_and_temperature_in_icfd"></a> Support viscosity and temperature in ICFD

### <a id="features_math"></a> Math

###### <a id="psd_1_sigma_operator"></a> PSD 1 sigma operator

### <a id="features_hdf5"></a> HDF5

###### <a id="cyclic_support_provider_from_hdf5"></a> Cyclic support provider from hdf5

###### <a id="incrementally_write_hdf5_fields"></a> Incrementally write HDF5 fields

###### <a id="importexport_of_string_fields_in_hdf5"></a> Import/Export of String fields in hdf5

### <a id="features_compression"></a> Compression

###### <a id="creation_of_sketch_matrix_operator"></a> Creation of Sketch matrix operator

### <a id="features_documentation"></a> Documentation

###### <a id="support_markdown_and_latex_in_chtmldocgenerator2"></a> Support Markdown and LaTeX in CHTML_Doc_Generator_2

### <a id="features_motion"></a> Motion

###### <a id="add_remote_point_name_in_the_dfmf_file"></a> Add remote point name in the dfmf file

### <a id="features_cgns"></a> CGNS

###### <a id="support_realsingle_datatype"></a> Support RealSingle datatype

Support `RealSingle` datatype in cgns files.


## Changes

### <a id="changes_framework"></a> Framework

###### <a id="changed_license_requirement_for_operator_splitfield"></a> Changed license requirement for operator split_field


Changed the license requirement for operator `split_field` from premium to entry.


###### <a id="report_key_collision_when_using_loadlibrary"></a> Report key collision when using load_library


Loading different plugins with same key now indicates something went wrong


###### <a id="enf_results_now_default_to_3d_vector_fields_instead_of_scalar_fields"></a> ENF results now default to 3D vector fields instead of scalar fields

###### <a id="remove_prints_when_dpf_server_is_starting"></a> Remove prints when DPF server is starting

### <a id="changes_hgp"></a> HGP

###### <a id="change_the_datatree_api_for_getting_attributes"></a> Change the DataTree API for getting attributes


Changing DataTree's API for getting attributes:
* Methods `get<type>Attribute` now have an optional default value as an input parameter. If the attribute does not exist, the default value will be returned. No error will be thrown.
* New methods `tryGet<type>Attribute` are now exposed, that return a boolean indicating if the attribute exist or not.


### <a id="changes_mapdl"></a> MAPDL

###### <a id="rename_magnetic_vector_potential_operator"></a> Rename magnetic vector potential operator

###### <a id="require_label_panel_in_the_modal_basis_for_expansion"></a> Require label "panel" in the modal basis for expansion

###### <a id="make_cyclic_operators_private"></a> Make cyclic operators private

### <a id="changes_cff"></a> CFF

###### <a id="add_prime_to_path_and_ldlibrarypath_in_cff_xml"></a> Add the Prime plugin as a dependency


The XML file for the CFF plugin now targets the Prime plugin as a dependency.


### <a id="changes_lsdyna"></a> LSDYNA

###### <a id="shell_layers_ordering"></a> Fix inconsistent shell layers ordering between LS-Dyna and DPF

LSDYNA results on shells with three integration points through the layer were ordered in an unexpected way, resulting in wrong behavior when changing the shell layer using `change_shell_layers`.
They now follow the DPF convention `[top, bottom, mid]`.
If more than three integration points are present in the shell, the regular LSDYNA ordering is kept (from bottom to top).

###### <a id="fix_bug_of_getting_erosion_mesh"></a> Erosion of the mesh is now tracked with an element status field

Erosion in the mesh was previously handled by storing the mesh connectivity at each step.
To imrpove performance and allow for bigger meshes with erosion, only the initial mesh is now stored, with a varying field of erosion element status.

### <a id="changes_hdf5"></a> HDF5

###### <a id="modifications_to_importexport_dpf_objects_for_hdf5"></a> Modifications to import/export dpf objects for hdf5

### <a id="changes_math"></a> Math

###### <a id="avoid_throwing_in_modalsolve_for_rhs_with_inputdofindex"></a> Avoid throwing in modal_solve for RHS with input_dof_index

###### <a id="fix_film_convetion_unit_unit_pow_shift"></a> Fix Film Convection Unit & unit pow shift

### <a id="changes_engineering_data"></a> Engineering Data

###### <a id="renamed_tsai_wu_constant_to_tsai_wu_constants"></a> Renamed Tsai Wu Constant to Tsai Wu Constants

## Fixes

### <a id="fixes_framework"></a> Framework

###### <a id="print_custom_type_collections"></a> print custom type collections

The string representation of DPF collections of custom types was always incorrectly reporting them as empty.


###### <a id="issue_with_node_averaged_results_with_scoping"></a> issue with node averaged results with scoping

###### <a id="fix_rescope_operator_for_input_fields_with_no_ids_in_the_scoping"></a> Fix Rescope operator for input fields with no ids in the scoping

###### <a id="crash_dpf_vector_commit"></a> Crash dpf vector commit

###### <a id="json_workflow_deserializer"></a> Json workflow deserializer

###### <a id="rtdldeepbind_flag_was_removed_from_dll_loading"></a> RTDL_DEEPBIND flag was removed from DLL loading

###### <a id="fix_location_of_averaged_empty_fields"></a> Fix location of averaged empty fields

###### <a id="allow_to_serialize_data_in_strings_for_more_than_2_gb"></a> Allow to serialize data in strings for more than 2 Gb


The "string_serializer" was limited to 2Gb strings output. A serialization mode "2" is created which allows to output several strings instead of one.


###### <a id="fix_skin_extraction_for_point_elements"></a> Fix skin extraction for point elements

Skin extraction missed some elements such as point. The fix added through an optional pin the possibility for the user to add those elements in the final mesh.


###### <a id="fixed_double_precision_issue_for_datatree_attributes_15__17_digits"></a> Fixed double precision issue for DataTree attributes (15 -> 17 digits)


Maximum guaranteed number of decimal digits in a double precision floating point number after comma is 17 (and not 15, apparently).
That's why [`max_digits10`](https://en.cppreference.com/w/cpp/types/numeric_limits/max_digits10) should be used instead of [`digits10`](https://en.cppreference.com/w/cpp/types/numeric_limits/digits10) for `double` and `vector<double>` serializations.


###### <a id="rescope_operator_acknowledges_only_first_duplicated_value"></a> rescope operator acknowledges only first duplicated value


Rescope operator acknowledges only first duplicated value.


###### <a id="improve_no_output_pin_error_message"></a> Improve no output pin error message


When an Operator output pin is not found, the error message is improved.


###### <a id="document_limitation_in_rotation_of_elemental_and_elementalnodal_results"></a> Document limitation in rotation of Elemental and ElementalNodal results


Document limitation in rotation of E and EN results (results may be incorrect).


###### <a id="allow_to_serialize_to_a_file_with_more_than_2gb"></a> Allow to serialize to a file with more than 2Gb


Fixes the "serializer" and "deserializer" operators to allow them to write files of more than 2 gB.


###### <a id="fix_load_plugin_error_code"></a> Fix load plugin error code


When loading a DPF plugin, the plugin can return an error code (int). This error code was not taken into account.


###### <a id="random_failure_on_license_checkout"></a> random failure on license checkout


Fix random crash on license checkout.


###### <a id="add_missing_support_for_nodal_fields_after_solidtoskin_operator"></a> Add missing support for nodal fields after solid-to-skin operator


The `solid_to_skin` operator did not properly set the support for node-centered fields.


###### <a id="fix_available_grpc_port_search_on_windows"></a> Fix available gRPC port search on Windows


Windows does not properly support reusing a socket port right after closing it. Server start now relies on gRPC finding available ports (it does not reuse closed ports directly).


###### <a id="close_windows_port_correctly_and_server_graceful_shutdown"></a> Close windows port correctly and server graceful shutdown


- Async gRPC server is now shutdown gracefully preventing random crashes
- When looking for available ports on windows, ports are correctly closed. They are now reused for next server.

###### <a id="fix_allocation_of_mesh_bitset_out_of_range"></a> Fix allocation of mesh bitset out of range


DPF mesh stores information on element types in a bitset. This bitset was allocated to a too small size and accessed out of range (memory corruption).


###### <a id="fix_splitshellssolid_to_correctly_propagate_shell_layers_if_skin_or_beam_elements_are_present"></a> Fix split_shells_solid to correctly propagate shell layers if skin or beam elements are present

###### <a id="fix_scoping_of_output_for_ascendingdescending_sorting_for_fieldscontainer"></a> Fix scoping of output for ascending/descending sorting for fieldscontainer

###### <a id="dynamically_test_for_cyclic_versions_of_source_operators"></a> Dynamically test for cyclic versions of source operators

###### <a id="fix_pin_splitshells_of_source_operators_with_elementalnodal_default_location_such_as_stress"></a> Fix pin `split_shells` of source operators with elemental_nodal default location such as `stress`

###### <a id="fix_naming_of_comparison_operators"></a> Fix naming of comparison operators

###### <a id="correctly_handle_empty_fields_in_changeshelllayers"></a> Correctly handle empty fields in `change_shell_layers`

###### <a id="fix_meshbyscoping_when_the_resulting_mesh_is_empty"></a> Fix `mesh.by_scoping` when the resulting mesh is empty

###### <a id="fix_shift_of_unit_with_the_power_function"></a> Fix shift of unit with the power function

###### <a id="fix_a_solidtoskin_mapping_issue_when_including_beamtype_elements"></a> Fix a solid-to-skin mapping issue when including beam-type elements

###### <a id="fix_load_plugin_error_reporting"></a> Fix load plugin error reporting.


### <a id="fixes_hgp"></a> HGP

###### <a id="fix_any_deep_copy_to_client"></a> Fix Any deep copy to client


The HGP API `Any::deep_copy` was not copying on a client, without returning an error. Copy on a client is now implemented for a local any.


###### <a id="fix_hgp_fielddefinitionsetdimensions"></a> Fix HGP FieldDefinition::setDimensions

###### <a id="remove_memory_leak_in_dpfvector_and_stringfield"></a> Remove memory leak in DpfVector and StringField

###### <a id="fix_dpfvector_subset_modification"></a> Fix DpfVector subset modification

###### <a id="fix_fielddefinitionunit_for_units_with_unknown_homogeneity"></a> Fix FieldDefinition.unit() for units with Unknown homogeneity

###### <a id="fix_customtypefieldsetdata"></a> Fix CustomTypeField.setData()

### <a id="fixes_mapdl"></a> MAPDL

###### <a id="solve_issue_with_reordering_of_unfiltered_enfs"></a> Solve issue with reordering of unfiltered ENFs

The unfiltered ENFs should not be reordered.


###### <a id="performance_issue_on_readmeshproperties"></a> Performance issue on readMeshProperties

Fix performance issue when reading mesh properties from the RST repeatedly.


###### <a id="fix_append_cyclic_support_on_engvolcyclic_and_nmisccyclic"></a> Fix append cyclic support on ENG_VOL_cyclic and NMISC_cyclic

Fix append cyclic support on ENG_VOL_cyclic and NMISC_cyclic.


###### <a id="nodal_averaged_result_operators_return_wrong_values_when_setting_a_mesh_scoping"></a> Nodal Averaged Result operators return wrong values when setting a mesh scoping

EPEL Nodal Averaged Results were null when provided with a scoping.


###### <a id="nodal_cyclic_expansion_creates_duplicated_scoping_ids"></a> Nodal cyclic expansion creates duplicated scoping ids

Nodal fields cyclic expansion created duplicated scoping ids.


###### <a id="do_not_read_wrong_cyclic_definition_id_offsets"></a> Do not read wrong cyclic definition id offsets

###### <a id="handle_gasket_degenerated_elements"></a> Handle Gasket Degenerated Elements

Handling INTER195 degenerated elements.
Handle combinations from keyopt8 & keyopt2 and verify that results available are expected.

###### <a id="fix_incorrect_dimension_when_reading_dsub_file"></a> Fix incorrect dimension when reading dsub file

Fixed incorrect dimension when reading dsub file, occasionally leading to random crashes in CMS expansion.

###### <a id="properly_initialize_the_shelllayer_obtained_for_elementalnodal_results"></a> Properly initialize the shellLayer obtained for ElementalNodal results

Initialize the shellLayer obtained for ElementalNodal results when reading Elemental results.
Fixed issue with the mesh for eShell elements, regarding eShellNumLayers.

###### <a id="fix_rotate_enf_results"></a> Fix rotate ENF results

In the case of an Harmonic, MSUP or modal analysis, three are three sets of ENF: STATIC, DAMPING and INERTIA
These sets are stored in the following order:
{Node1: FSX, FSY, FSZ}, {Node2: FSX, FSY, FSZ}, ..., {Node1: FDX, FDY, FDZ}, {Node2: FDX, FDY, FDZ}, ...,{Node1: FIX, FIY, FIZ}, {Node2: FIX, FIY, FIZ}, ...

For these cases, if the analysis was cyclic or if the pin reorderENF was set to true a reordering was done and the number of components was set to 9.

_(The reordered ENF is in the following order:
{Node1: FSX, FSY, FSZ, FDX, FDY, FDZ, FIX, FIY, FIZ}, {Node2: FSX, FSY, FSZ, FDX, FDY, FDZ, FIX, FIY, FIZ}, ...)_

So if the analysis was Harmonic, MSUP or modal but not cyclic the number of components would be 3 but each node would have 9 values. That would later throw an error.

In order to be able to do the rotation, we reorder the ENFs if they are not already ordered before rotating them. Them we put them back in their initial ordering state.

The number of components is now always set to 1 if we are reading unfiltered data.

###### <a id="fix_bugs_for_msup_harmonic_analysis_with_mode_file_scoping"></a> Fix bugs for MSUP harmonic analysis with MODE file scoping

###### <a id="rescyclic_operators_can_now_average_from_elementalnodal_to_elemental"></a> RES_cyclic operators can now average from elemental_nodal to elemental

`RES_Cyclic` operators average to elemental from elemental_nodal.
Elemental `mesh_scoping` not working for cyclic energies.


###### <a id="repair_mapdlrstmeshpropertyprovider"></a> Repair mesh_property_provider for RST files

Fix crash on reading distributed files through `mesh_property_provider` operator for RST files.


###### <a id="fix_shell_layer_management_for_stress_results_on_elements_181_and_281"></a> Fix shell layer management for stress results on elements 181 and 281

Two issues were observed:
- Reading stress results for elements 181 and 281 (one for field), was giving a nonelayer for its shell_layers.
- Setting the Elemental input for the requested location gives an empty field.


###### <a id="modaldampingratio_operator_is_outputting_nan_when_natural_frequency_is_exactly_0"></a> modal_damping_ratio operator is outputting NaN when Natural Frequency is exactly 0


###### <a id="infinite_loop_in_function_readenfresultblock"></a> Infinite loop in function readENFResultBlock

###### <a id="fix_an_issue_with_index_in_elemental_rotation"></a> Fix an issue with index in elemental rotation

###### <a id="add_mesh_to_elemental_energy_results_from_mapdl"></a> Add mesh to elemental energy results from MAPDL

###### <a id="fix_beam_material_property_retrieval_for_unmatching_section_and_material_id"></a> Fix beam material property retrieval for unmatching section and material ID

###### <a id="fix_a_crash_for_operator_coordsandeulernodes_when_the_input_scoping_is_empty"></a> Fix a crash for operator coords_and_euler_nodes when the input scoping is empty

###### <a id="solve_issue_with_ectstat_results_reading"></a> Solve issue with ECT_STAT results reading

###### <a id="fix_a_crash_in_mode_contribution_operator"></a> Fix a crash in mode contribution operator

###### <a id="fix_an_inconsistency_in_results_between_cyclic_operators_using_a_stream_and_using_a_datasources"></a> Fix an inconsistency in results between cyclic operators using a stream and using a datasources

###### <a id="fix_a_dmp_crash_for_mode_file_scoping"></a> Fix a dmp crash for mode file scoping

###### <a id="fix_mapdl_run_cmd_issue_input_missing"></a> Fix mapdl run cmd issue "input missing"

### <a id="fixes_cff"></a> CFF

###### <a id="mark_cff_unsupported_elements_as_polyhedrons"></a> Mark CFF unsupported elements as Polyhedrons


Mark CFF unsupported elements as Polyhedrons. These elements are marked in the CFF file with cell types outside of the CffCellType enum.


###### <a id="missing_data_for_cff_resultinfo"></a> Missing data for CFF ResultInfo


Some results were wrong or missing in the CFF result info.
Using the CFFSDK reader, we now expose available results as consistently as possible.


### <a id="fixes_lsdyna"></a> LSDYNA

###### <a id="fix_issue_for_lsda_on_linux"></a> Fix a crash on Linux with gcc 8 for LSDA operators

###### <a id="pr_lsda_normalvel"></a> Fix LSDA imports and exports for 1D frequency data

###### <a id="fix_problem_of_extracting_binout_nodfor_group_data"></a> Fix an issue when extracting BINOUT NODFOR data

###### <a id="fix_bug_of_extracting_strain_data"></a> Fix a crash when reading total_strain from d3plot for shells with more than 3 IP in the thickness

###### <a id="fix_bug_of_extracting_displacements_from_d3plots_that_contain_em_data"></a> Fix extraction of displacements from d3plot files with electro-magnetic data

###### <a id="pr_tshell"></a> Fix reading the mesh connectivity for TSHELL

###### <a id="fix_bug_for_getting_erosion_data"></a> Fix a bug when reading erosion data by part

###### <a id="support_writing_lsda_file_larger_than_2gb"></a> Support writing LSDA files larger than 2GB

### <a id="fixes_math"></a> Math

###### <a id="fix_matrixmatrix_product_for_symmetrical_matrices_extra_diagonal_terms_were_divided_by_2"></a> Fix matrix-matrix product for symmetrical matrices (extra diagonal terms were divided by 2)

### <a id="fixes_hdf5"></a> HDF5

###### <a id="custom_type_fields_hdf5_exportimport_to_read_the_type_of_data"></a> Custom Type Fields hdf5 export/import to read the type of data

Custom Type Fields hdf5 export/import to read the type of data.

###### <a id="fix_out_of_bound_access_in_hdf5_append"></a> Fix out of bound access in HDF5 append

###### <a id="fix_corner_node_filteringextrapolation"></a> Fix corner node filtering/extrapolation

###### <a id="fix_missing_error_message_when_reading_an_inexistant_custom_result"></a> Fix missing error message when reading an inexistant custom result


When reading a custom result from HDF5, the error was reported as "unknown exception occurred". It is now explicit.


###### <a id="hdf5_fix_the_tfs_data_pointer_not_being_properly_expanded"></a> HDF5: Fix the TFS' data pointer not being properly expanded


###### <a id="read_hdf5_file_without_license_check"></a> Read Hdf5 file without license check


Allow to read Hdf5 file that contains a workflow without license check.


###### <a id="fix_hdf5_streamprovider_operator_doesnt_check_the_file_existence"></a> Fix hdf5 stream_provider operator doesn't check the file existence


The operator `stream_provider` now throws an error in case of an invalid file path.

###### <a id="fix_adding_empty_meshregion_crashes_writing_to_hdf5"></a> Fix adding empty MeshRegion crashes writing to hdf5

### <a id="fixes_vtk"></a> VTK

###### <a id="improve_vtu_export_for_several_field_inputs"></a> Improve VTU export for several field inputs


- "vtu_export" operator produces invalid vtu when one unnamed over time fields container and one unnamed property field are exported. This is due to name clash.
- "vtu_export" operator exports 2 files when one field, one property field and one fields container with a single time are exported. It should only export one


## Performance Improvements

### <a id="performance_framework"></a> Framework

###### <a id="improve_memory_allocation_in_operator_splitfields"></a> Improve memory allocation in operator `split_fields`


Improving memory allocation in operator `split_fields`.


###### <a id="customtypefields_with_double_values_are_now_better_handling_huge_sizes"></a> CustomTypeFields with double values are now better handling huge sizes


`CustomTypeField` are not producing errors anymore when using a high number of double values.


###### <a id="improve_performance_of_solidtoskin"></a> Improve performance of `solid_to_skin`

###### <a id="improve_performance_of_scoping_transposition_with_a_new_cache_logic"></a> Improve performance of scoping transposition with a new cache logic

###### <a id="improve_performance_of_dpfvector"></a> Improve performance of DpfVector

###### <a id="improve_performance_of_the_splitonpropertytype_operator_for_multiple_properties"></a> Improve performance of the `split_on_property_type` operator for multiple properties

###### <a id="improve_performance_of_the_changelshelllayers_operator"></a> Improve performance of the `change_shell_layers` operator

###### <a id="improve_performance_when_getting_a_unit_symbol"></a> Improve performance when getting a unit symbol

###### <a id="improve_performance_of_anycollection_by_not_casting_to_any_first"></a> Improve performance of AnyCollection by not casting to Any first

### <a id="performance_hgp"></a> HGP

###### <a id="prevent_useless_memory_allocation_when_creating_an_empty_dpfvector_"></a> Prevent useless memory allocation when creating an empty DpfVector

###### <a id="improve_performance_of_the_datatree"></a> Improve performance of the DataTree

### <a id="performance_mapdl"></a> MAPDL

###### <a id="solve_property_field_provider_by_name_performance_issues_with_distributed_files"></a> Solve property field provider by name performance issues with distributed files

###### <a id="improved_performance_when_recovering_element_results"></a> Improved performance when recovering element results

Modifications to solve performance issue when recovering element results.

###### <a id="improve_performances_when_reading_modal_results_in_mechanical_with_dpf"></a> Improve performances when reading modal results in Mechanical with DPF

### <a id="performance_compression"></a> Compression

###### <a id="avoid_reserving_more_data_than_needed_for_zstd_decompression"></a> Avoid reserving more data than needed for ZSTD decompression
