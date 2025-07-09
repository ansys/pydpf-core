#-------------------------------------------------------------------------------
# Any
#-------------------------------------------------------------------------------

class AnyAbstractAPI:
	@staticmethod
	def init_any_environment(object):
		pass

	@staticmethod
	def finish_any_environment(object):
		pass

	@staticmethod
	def any_wrapped_type_string(data):
		raise NotImplementedError

	@staticmethod
	def any_object_is_of_type(data, type_name):
		raise NotImplementedError

	@staticmethod
	def any_unwrap_to_real_type(dpf_object):
		raise NotImplementedError

	@staticmethod
	def any_get_as_fields_container(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_scopings_container(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_field(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_scoping(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_data_sources(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_meshes_container(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_any_collection(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_string(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_string_with_size(any, size):
		raise NotImplementedError

	@staticmethod
	def any_get_as_int(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_double(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_int_collection(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_double_collection(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_cyclic_support(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_workflow(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_time_freq_support(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_meshed_region(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_result_info(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_materials_container(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_streams(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_property_field(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_data_tree(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_operator(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_string_field(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_generic_data_container(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_custom_type_fields_container(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_custom_type_field(any):
		raise NotImplementedError

	@staticmethod
	def any_get_as_support(any):
		raise NotImplementedError

	@staticmethod
	def any_make_obj_as_any(dpf_object):
		raise NotImplementedError

	@staticmethod
	def any_new_from_int(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_string(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_string_with_size(any, size):
		raise NotImplementedError

	@staticmethod
	def any_new_from_double(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_fields_container(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_scopings_container(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_field(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_scoping(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_data_sources(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_meshes_container(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_int_collection(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_double_collection(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_cyclic_support(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_workflow(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_time_freq_support(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_meshed_region(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_result_info(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_materials_container(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_streams(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_property_field(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_data_tree(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_operator(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_string_field(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_generic_data_container(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_custom_type_fields_container(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_custom_type_field(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_any_collection(any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_int_on_client(client, value):
		raise NotImplementedError

	@staticmethod
	def any_new_from_string_on_client(client, any):
		raise NotImplementedError

	@staticmethod
	def any_new_from_string_with_size_on_client(client, any, size):
		raise NotImplementedError

	@staticmethod
	def any_new_from_double_on_client(client, any):
		raise NotImplementedError

	@staticmethod
	def any_get_copy(id, client):
		raise NotImplementedError

