#-------------------------------------------------------------------------------
# DpfDataTree
#-------------------------------------------------------------------------------

class DpfDataTreeAbstractAPI:
	@staticmethod
	def init_dpf_data_tree_environment(object):
		pass

	@staticmethod
	def finish_dpf_data_tree_environment(object):
		pass

	@staticmethod
	def dpf_data_tree_new():
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_delete(data_tree):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_has_sub_tree(data_tree, sub_tree_name):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_sub_tree(data_tree, sub_tree_name):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_make_sub_tree(data_tree, sub_tree_name):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_has_attribute(data_tree, attribute_name):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_available_attributes_names_in_string_collection(data_tree):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_available_sub_tree_names_in_string_collection(data_tree):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_int_attribute(data_tree, attribute_name, value):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_unsigned_int_attribute(data_tree, attribute_name, value):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_double_attribute(data_tree, attribute_name, value):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_string_attribute(data_tree, attribute_name, data, size):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_vec_int_attribute(data_tree, attribute_name, data, size):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_vec_double_attribute(data_tree, attribute_name, data, size):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_int_attribute_with_check(data_tree, attribute_name, value, value_found):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_unsigned_int_attribute_with_check(data_tree, attribute_name, value, value_found):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_double_attribute_with_check(data_tree, attribute_name, value, value_found):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_string_attribute_with_check(data_tree, attribute_name, data, size, value_found):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_vec_int_attribute_with_check(data_tree, attribute_name, data, size, value_found):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_vec_double_attribute_with_check(data_tree, attribute_name, data, size, value_found):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_string_collection_attribute(data_tree, attribute_name):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_get_string_collection_attribute_with_check(data_tree, attribute_name, value_found):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_set_int_attribute(data_tree, attribute_name, value):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_set_unsigned_int_attribute(data_tree, attribute_name, value):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_set_vec_int_attribute(data_tree, attribute_name, value, size):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_set_double_attribute(data_tree, attribute_name, value):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_set_vec_double_attribute(data_tree, attribute_name, value, size):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_set_string_collection_attribute(data_tree, attribute_name, collection):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_set_string_attribute(data_tree, attribute_name, data, size):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_set_sub_tree_attribute(data_tree, attribute_name, data):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_save_to_txt(dataSources, text, size):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_read_from_text(dataSources, filename, size):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_save_to_json(dataSources, text, size):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_read_from_json(dataSources, filename):
		raise NotImplementedError

	@staticmethod
	def dpf_data_tree_new_on_client(client):
		raise NotImplementedError

