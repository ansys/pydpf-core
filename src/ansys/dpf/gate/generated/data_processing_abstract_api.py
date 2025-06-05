#-------------------------------------------------------------------------------
# DataProcessing
#-------------------------------------------------------------------------------

class DataProcessingAbstractAPI:
	@staticmethod
	def init_data_processing_environment(object):
		pass

	@staticmethod
	def finish_data_processing_environment(object):
		pass

	@staticmethod
	def data_processing_initialization():
		raise NotImplementedError

	@staticmethod
	def data_processing_release(context):
		raise NotImplementedError

	@staticmethod
	def data_processing_initialize_with_context(context, xml_path):
		raise NotImplementedError

	@staticmethod
	def data_processing_initialize_with_context_v2(var1):
		raise NotImplementedError

	@staticmethod
	def data_processing_apply_context(context, xml_path):
		raise NotImplementedError

	@staticmethod
	def data_processing_apply_context_v2(context_data):
		raise NotImplementedError

	@staticmethod
	def data_processing_set_debug_trace(text):
		raise NotImplementedError

	@staticmethod
	def data_processing_set_trace_section(text):
		raise NotImplementedError

	@staticmethod
	def data_processing_load_library(name, dllPath, symbol):
		raise NotImplementedError

	@staticmethod
	def data_processing_available_operators():
		raise NotImplementedError

	@staticmethod
	def data_processing_duplicate_object_reference(base):
		raise NotImplementedError

	@staticmethod
	def data_processing_objects_holds_same_data(a, b):
		raise NotImplementedError

	@staticmethod
	def data_processing_wrap_unknown(data, destructor, type_hash):
		raise NotImplementedError

	@staticmethod
	def data_processing_unwrap_unknown(data, expected_type_hash):
		raise NotImplementedError

	@staticmethod
	def data_processing_delete_shared_object(data):
		raise NotImplementedError

	@staticmethod
	def data_processing_delete_shared_object_array(data, size):
		raise NotImplementedError

	@staticmethod
	def data_processing_unknown_has_given_hash(data, expected_type_hash):
		raise NotImplementedError

	@staticmethod
	def data_processing_description_string(data):
		raise NotImplementedError

	@staticmethod
	def data_processing_description_string_with_size(data, size):
		raise NotImplementedError

	@staticmethod
	def data_processing_delete_string(var1):
		raise NotImplementedError

	@staticmethod
	def data_processing_string_post_event(output):
		raise NotImplementedError

	@staticmethod
	def data_processing_list_operators_as_collection():
		raise NotImplementedError

	@staticmethod
	def data_processing_free_ints(data):
		raise NotImplementedError

	@staticmethod
	def data_processing_free_doubles(data):
		raise NotImplementedError

	@staticmethod
	def data_processing_serialize(obj):
		raise NotImplementedError

	@staticmethod
	def data_processing_deserialize(data, dataSize):
		raise NotImplementedError

	@staticmethod
	def data_processing_deserialize_many(str, strSize, size):
		raise NotImplementedError

	@staticmethod
	def data_processing_get_global_config_as_data_tree():
		raise NotImplementedError

	@staticmethod
	def data_processing_get_server_version(major, minor):
		raise NotImplementedError

	@staticmethod
	def data_processing_get_os():
		raise NotImplementedError

	@staticmethod
	def data_processing_process_id():
		raise NotImplementedError

	@staticmethod
	def data_processing_create_param_tree():
		raise NotImplementedError

	@staticmethod
	def data_processing_logging_register_logger(register_logger_params):
		raise NotImplementedError

	@staticmethod
	def data_processing_logging_get_logger(get_logger_params):
		raise NotImplementedError

	@staticmethod
	def data_processing_logging_log_message(logger_impl, message, log_level):
		raise NotImplementedError

	@staticmethod
	def data_processing_logging_flush(logger_impl):
		raise NotImplementedError

	@staticmethod
	def data_processing_logging_flush_all():
		raise NotImplementedError

	@staticmethod
	def data_processing_initialization_on_client(client):
		raise NotImplementedError

	@staticmethod
	def data_processing_release_on_client(client, context):
		raise NotImplementedError

	@staticmethod
	def data_processing_initialize_with_context_on_client(client, context, dataProcessingCore_xml_path):
		raise NotImplementedError

	@staticmethod
	def data_processing_apply_context_on_client(client, context, dataProcessingCore_xml_path):
		raise NotImplementedError

	@staticmethod
	def data_processing_apply_context_v2_on_client(client, context_data):
		raise NotImplementedError

	@staticmethod
	def data_processing_load_library_on_client(sLibraryKey, sDllPath, sloader_symbol, client):
		raise NotImplementedError

	@staticmethod
	def data_processing_get_id_of_duplicate_object_reference(base):
		raise NotImplementedError

	@staticmethod
	def data_processing_release_obj_by_id_in_db(id, client, bAsync):
		raise NotImplementedError

	@staticmethod
	def data_processing_delete_string_for_object(api_to_use, var1):
		raise NotImplementedError

	@staticmethod
	def data_processing_get_client(base):
		raise NotImplementedError

	@staticmethod
	def data_processing_prepare_shutdown(client):
		raise NotImplementedError

	@staticmethod
	def data_processing_release_server(client):
		raise NotImplementedError

	@staticmethod
	def data_processing_string_post_event_for_object(api_to_use, output):
		raise NotImplementedError

	@staticmethod
	def data_processing_free_ints_for_object(api_to_use, data):
		raise NotImplementedError

	@staticmethod
	def data_processing_free_doubles_for_object(api_to_use, data):
		raise NotImplementedError

	@staticmethod
	def data_processing_deserialize_on_client(client, data, dataSize):
		raise NotImplementedError

	@staticmethod
	def data_processing_get_global_config_as_data_tree_on_client(client):
		raise NotImplementedError

	@staticmethod
	def data_processing_get_client_config_as_data_tree():
		raise NotImplementedError

	@staticmethod
	def data_processing_get_server_version_on_client(client, major, minor):
		raise NotImplementedError

	@staticmethod
	def data_processing_get_server_ip_and_port(client, port):
		raise NotImplementedError

	@staticmethod
	def data_processing_get_os_on_client(client):
		raise NotImplementedError

	@staticmethod
	def data_processing_download_file(client, server_file_path, to_client_file_path):
		raise NotImplementedError

	@staticmethod
	def data_processing_download_files(client, server_file_path, to_client_file_path, specific_extension):
		raise NotImplementedError

	@staticmethod
	def data_processing_list_operators_as_collection_on_client(client):
		raise NotImplementedError

	@staticmethod
	def data_processing_upload_file(client, file_path, to_server_file_path, use_tmp_dir):
		raise NotImplementedError

	@staticmethod
	def data_processing_process_id_on_client(client):
		raise NotImplementedError

	@staticmethod
	def data_processing_create_param_tree_on_client(client):
		raise NotImplementedError

	@staticmethod
	def data_processing_create_from_on_client(client, base):
		raise NotImplementedError

