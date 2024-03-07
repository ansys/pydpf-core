#-------------------------------------------------------------------------------
# Operator
#-------------------------------------------------------------------------------

class OperatorAbstractAPI:
	@staticmethod
	def init_operator_environment(object):
		pass

	@staticmethod
	def finish_operator_environment(object):
		pass

	@staticmethod
	def operator_new(operatorName):
		raise NotImplementedError

	@staticmethod
	def operator_get_specification_if_any(operatorName):
		raise NotImplementedError

	@staticmethod
	def operator_delete(op):
		raise NotImplementedError

	@staticmethod
	def operator_record_instance(op, transfer_ownership):
		raise NotImplementedError

	@staticmethod
	def operator_record_with_new_name(existing_identifier, new_identifier, core):
		raise NotImplementedError

	@staticmethod
	def operator_set_config(op, config):
		raise NotImplementedError

	@staticmethod
	def operator_get_config(op):
		raise NotImplementedError

	@staticmethod
	def operator_by_id(id):
		raise NotImplementedError

	@staticmethod
	def get_operator_id(op):
		raise NotImplementedError

	@staticmethod
	def dpf_operator_by_name(operatorName):
		raise NotImplementedError

	@staticmethod
	def dpf_operator_delete(op):
		raise NotImplementedError

	@staticmethod
	def operator_connect_dpf_type(op, iPin, value):
		raise NotImplementedError

	@staticmethod
	def operator_connect_int(op, iPin, value):
		raise NotImplementedError

	@staticmethod
	def operator_connect_bool(op, iPin, value):
		raise NotImplementedError

	@staticmethod
	def operator_connect_double(op, iPin, value):
		raise NotImplementedError

	@staticmethod
	def operator_connect_string(op, iPin, value):
		raise NotImplementedError

	@staticmethod
	def operator_connect_string_with_size(op, iPin, value, size):
		raise NotImplementedError

	@staticmethod
	def operator_connect_scoping(op, iPin, scoping):
		raise NotImplementedError

	@staticmethod
	def operator_connect_data_sources(op, iPin, dataSources):
		raise NotImplementedError

	@staticmethod
	def operator_connect_field(op, iPin, value):
		raise NotImplementedError

	@staticmethod
	def operator_connect_collection(op, iPin, value):
		raise NotImplementedError

	@staticmethod
	def operator_connect_meshed_region(op, iPin, dataSources):
		raise NotImplementedError

	@staticmethod
	def operator_connect_vector_int(op, iPin, ptrValue, size):
		raise NotImplementedError

	@staticmethod
	def operator_connect_vector_double(op, iPin, ptrValue, size):
		raise NotImplementedError

	@staticmethod
	def operator_connect_collection_as_vector(op, iPin, collection):
		raise NotImplementedError

	@staticmethod
	def operator_connect_operator_output(op, iPin, value, outputIndex):
		raise NotImplementedError

	@staticmethod
	def operator_connect_streams(op, iPin, streams):
		raise NotImplementedError

	@staticmethod
	def operator_connect_property_field(op, iPin, streams):
		raise NotImplementedError

	@staticmethod
	def operator_connect_string_field(op, iPin, value):
		raise NotImplementedError

	@staticmethod
	def operator_connect_custom_type_field(op, iPin, value):
		raise NotImplementedError

	@staticmethod
	def operator_connect_support(op, iPin, support):
		raise NotImplementedError

	@staticmethod
	def operator_connect_time_freq_support(op, iPin, support):
		raise NotImplementedError

	@staticmethod
	def operator_connect_workflow(op, iPin, wf):
		raise NotImplementedError

	@staticmethod
	def operator_connect_cyclic_support(op, iPin, sup):
		raise NotImplementedError

	@staticmethod
	def operator_connect_ians_dispatch(op, iPin, ptr):
		raise NotImplementedError

	@staticmethod
	def operator_connect_data_tree(op, iPin, ptr):
		raise NotImplementedError

	@staticmethod
	def operator_connect_external_data(op, iPin, ptr):
		raise NotImplementedError

	@staticmethod
	def operator_connect_remote_workflow(op, iPin, ptr):
		raise NotImplementedError

	@staticmethod
	def operator_connect_operator_as_input(op, iPin, ptr):
		raise NotImplementedError

	@staticmethod
	def operator_connect_any(op, iPin, ptr):
		raise NotImplementedError

	@staticmethod
	def operator_connect_label_space(op, iPin, ptr):
		raise NotImplementedError

	@staticmethod
	def operator_connect_generic_data_container(op, iPin, ptr):
		raise NotImplementedError

	@staticmethod
	def operator_connect_result_info(op, iPin, ptr):
		raise NotImplementedError

	@staticmethod
	def operator_disconnect(op, iPin):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_fields_container(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_scopings_container(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_field(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_scoping(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_data_sources(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_field_mapping(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_meshes_container(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_custom_type_fields_container(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_cyclic_support(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_workflow(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_string_field(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_custom_type_field(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_generic_data_container(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_string(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_string_with_size(op, iOutput, size):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_bytearray(op, iOutput, size):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_int(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_double(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_bool(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_time_freq_support(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_meshed_region(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_result_info(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_materials_container(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_streams(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_property_field(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_any_support(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_data_tree(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_operator(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_external_data(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_int_collection(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_double_collection(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_getoutput_as_any(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_has_output_when_evaluated(op, iOutput):
		raise NotImplementedError

	@staticmethod
	def operator_status(op):
		raise NotImplementedError

	@staticmethod
	def operator_run(op):
		raise NotImplementedError

	@staticmethod
	def operator_invalidate(op):
		raise NotImplementedError

	@staticmethod
	def operator_derivate(op):
		raise NotImplementedError

	@staticmethod
	def operator_name(op):
		raise NotImplementedError

	@staticmethod
	def operator_get_status(op):
		raise NotImplementedError

	@staticmethod
	def operator_new_on_client(operatorName, client):
		raise NotImplementedError

	@staticmethod
	def operator_get_copy(id, client):
		raise NotImplementedError

	@staticmethod
	def operator_get_id_for_client(wf):
		raise NotImplementedError

