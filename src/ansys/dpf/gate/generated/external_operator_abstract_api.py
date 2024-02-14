#-------------------------------------------------------------------------------
# ExternalOperator
#-------------------------------------------------------------------------------

class ExternalOperatorAbstractAPI:
	@staticmethod
	def init_external_operator_environment(object):
		pass

	@staticmethod
	def finish_external_operator_environment(object):
		pass

	@staticmethod
	def external_operator_record(operator_main, func, operator_identifier, spec):
		raise NotImplementedError

	@staticmethod
	def external_operator_record_with_abstract_core(operator_main, func, operator_identifier, spec, core):
		raise NotImplementedError

	@staticmethod
	def external_operator_record_with_abstract_core_and_wrapper(operator_main, func, operator_identifier, spec, core, wrapper):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_status(operator_data, status):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_exception(operator_data, error_code, message):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_collection(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_num_inputs(operator_data):
		raise NotImplementedError

	@staticmethod
	def external_operator_has_input(operator_data, index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_field(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_field(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_fields_container(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_data_sources(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_data_sources(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_scoping(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_scoping(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_scopings_container(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_meshed_region(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_meshed_region(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_time_freq(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_time_freq(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_meshes_container(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_custom_type_fields_container(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_streams(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_streams(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_property_field(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_generic_data_container(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_property_field(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_support(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_data_tree(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_workflow(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_operator(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_external_data(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_as_any(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_remote_workflow(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_remote_operator(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_string_field(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_custom_type_field(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_label_space(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_remote_workflow(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_operator(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_support(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_as_any(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_bool(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_bool(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_int(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_int(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_double(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_double(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_long_long(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_long_long(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_string(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_string(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_string_with_size(operator_data, pin_index, size):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_string_with_size(operator_data, pin_index, data, size):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_vec_int(operator_data, pin_index, size):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_vecint(operator_data, pin_index, data, size):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_vec_double(operator_data, pin_index, size):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_in_vec_string_as_collection(operator_data, pin_index):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_data_tree(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_workflow(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_generic_data_container(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_result_info(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_string_field(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_custom_type_field(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_external_data(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_put_out_collection_as_vector(operator_data, pin_index, data):
		raise NotImplementedError

	@staticmethod
	def external_operator_pin_is_of_type(operator_data, pin_index, type_name):
		raise NotImplementedError

	@staticmethod
	def external_operator_delegate_run(operator_data, other_op, forwardInputs):
		raise NotImplementedError

	@staticmethod
	def external_operator_connect_all_inputs_to_operator(operator_data, other_op):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_operator_name(operator_data):
		raise NotImplementedError

	@staticmethod
	def external_operator_get_operator_config(operator_data):
		raise NotImplementedError

