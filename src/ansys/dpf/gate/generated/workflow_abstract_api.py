#-------------------------------------------------------------------------------
# Workflow
#-------------------------------------------------------------------------------

class WorkflowAbstractAPI:
	@staticmethod
	def init_workflow_environment(object):
		pass

	@staticmethod
	def finish_workflow_environment(object):
		pass

	@staticmethod
	def work_flow_new():
		raise NotImplementedError

	@staticmethod
	def work_flow_get_copy(wf):
		raise NotImplementedError

	@staticmethod
	def work_flow_create_from_text(text):
		raise NotImplementedError

	@staticmethod
	def work_flow_get_copy_on_other_client(wf, client, protocol):
		raise NotImplementedError

	@staticmethod
	def work_flow_delete(wf):
		raise NotImplementedError

	@staticmethod
	def work_flow_record_instance(wf, user_name, transfer_ownership):
		raise NotImplementedError

	@staticmethod
	def work_flow_replace_instance_at_id(wf, id, user_name, transfer_ownership):
		raise NotImplementedError

	@staticmethod
	def work_flow_erase_instance(wf):
		raise NotImplementedError

	@staticmethod
	def work_flow_get_record_id(wf):
		raise NotImplementedError

	@staticmethod
	def work_flow_get_by_identifier(identifier):
		raise NotImplementedError

	@staticmethod
	def work_flow_get_first_op(wf):
		raise NotImplementedError

	@staticmethod
	def work_flow_get_last_op(wf):
		raise NotImplementedError

	@staticmethod
	def work_flow_discover_operators(wf):
		raise NotImplementedError

	@staticmethod
	def work_flow_chain_with(wf, wf2):
		raise NotImplementedError

	@staticmethod
	def work_flow_chain_with_specified_names(wf, wf2, input_name, output_name):
		raise NotImplementedError

	@staticmethod
	def workflow_create_connection_map():
		raise NotImplementedError

	@staticmethod
	def workflow_add_entry_connection_map(map, out, in_):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_with(wf_right, wf2_left):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_with_specified_names(wf_right, wf2_left, map):
		raise NotImplementedError

	@staticmethod
	def work_flow_add_operator(wf, op):
		raise NotImplementedError

	@staticmethod
	def work_flow_number_of_operators(wf):
		raise NotImplementedError

	@staticmethod
	def work_flow_operator_name_by_index(wf, op_index):
		raise NotImplementedError

	@staticmethod
	def work_flow_set_name_input_pin(wf, op, pin, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_set_name_output_pin(wf, op, pin, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_rename_input_pin(wf, pin_name, new_pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_rename_output_pin(wf, pin_name, new_pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_erase_input_pin(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_erase_output_pin(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_has_input_pin(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_has_output_pin(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_number_of_input(wf):
		raise NotImplementedError

	@staticmethod
	def work_flow_number_of_output(wf):
		raise NotImplementedError

	@staticmethod
	def work_flow_input_by_index(wf, pin_index):
		raise NotImplementedError

	@staticmethod
	def work_flow_output_by_index(wf, pin_index):
		raise NotImplementedError

	@staticmethod
	def work_flow_number_of_symbol(wf):
		raise NotImplementedError

	@staticmethod
	def work_flow_symbol_by_index(wf, symbol_index):
		raise NotImplementedError

	@staticmethod
	def work_flow_generate_all_derivatives_for(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_generate_derivatives_for(wf, pin_name, variable_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_write_swf(wf, file_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_load_swf(wf, file_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_write_swf_utf8(wf, file_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_load_swf_utf8(wf, file_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_write_to_text(wf):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_dpf_type(wf, pin_name, value):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_int(wf, pin_name, value):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_bool(wf, pin_name, value):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_double(wf, pin_name, value):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_string(wf, pin_name, value):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_string_with_size(wf, pin_name, value, size):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_scoping(wf, pin_name, scoping):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_data_sources(wf, pin_name, dataSources):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_streams(wf, pin_name, dataSources):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_field(wf, pin_name, value):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_collection(wf, pin_name, value):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_collection_as_vector(wf, pin_name, value):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_meshed_region(wf, pin_name, mesh):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_property_field(wf, pin_name, field):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_string_field(wf, pin_name, field):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_custom_type_field(wf, pin_name, field):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_support(wf, pin_name, support):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_cyclic_support(wf, pin_name, support):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_time_freq_support(wf, pin_name, support):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_workflow(wf, pin_name, otherwf):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_remote_workflow(wf, pin_name, otherwf):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_vector_int(wf, pin_name, ptrValue, size):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_vector_double(wf, pin_name, ptrValue, size):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_operator_output(wf, pin_name, value, output_pin):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_external_data(wf, pin_name, dataSources):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_data_tree(wf, pin_name, dataTree):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_any(wf, pin_name, any):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_label_space(wf, pin_name, labelspace):
		raise NotImplementedError

	@staticmethod
	def work_flow_connect_generic_data_container(wf, pin_name, labelspace):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_fields_container(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_scopings_container(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_field(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_scoping(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_time_freq_support(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_meshes_container(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_meshed_region(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_result_info(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_property_field(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_any_support(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_cyclic_support(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_data_sources(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_streams(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_workflow(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_external_data(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_as_any(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_int_collection(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_double_collection(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_operator(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_string_field(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_custom_type_field(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_custom_type_fields_container(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_data_tree(op, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_generic_data_container(op, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_unit(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_string(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_string_with_size(wf, pin_name, size):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_int(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_double(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_getoutput_bool(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_has_output_when_evaluated(wf, pin_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_add_tag(wf, tag_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_has_tag(wf, tag_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_export_graphviz(wf, utf8_filename):
		raise NotImplementedError

	@staticmethod
	def work_flow_export_json(wf, text, size):
		raise NotImplementedError

	@staticmethod
	def work_flow_import_json(wf, text, size):
		raise NotImplementedError

	@staticmethod
	def work_flow_make_from_template(template_name):
		raise NotImplementedError

	@staticmethod
	def work_flow_template_exists(template_name):
		raise NotImplementedError

	@staticmethod
	def workflow_get_operators_collection_for_input(wf, input_name, pin_indexes, size):
		raise NotImplementedError

	@staticmethod
	def workflow_get_operator_for_output(wf, output_name, pin_index):
		raise NotImplementedError

	@staticmethod
	def workflow_get_client_id(wf):
		raise NotImplementedError

	@staticmethod
	def work_flow_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def work_flow_create_from_text_on_client(text, client):
		raise NotImplementedError

	@staticmethod
	def work_flow_get_copy_on_client(id, client):
		raise NotImplementedError

	@staticmethod
	def work_flow_get_by_identifier_on_client(identifier, client):
		raise NotImplementedError

	@staticmethod
	def workflow_create_connection_map_for_object(api_to_use):
		raise NotImplementedError

