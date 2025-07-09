#-------------------------------------------------------------------------------
# DpfVector
#-------------------------------------------------------------------------------

class DpfVectorAbstractAPI:
	@staticmethod
	def init_dpf_vector_environment(object):
		pass

	@staticmethod
	def finish_dpf_vector_environment(object):
		pass

	@staticmethod
	def dpf_vector_new():
		raise NotImplementedError

	@staticmethod
	def dpf_vector_double_free(dpf_vector, data, size, modified):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_char_free(dpf_vector, data, size, modified):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_int_free(dpf_vector, data, size, modified):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_char_ptr_free_with_size(dpf_vector, data, sizes, size, modified):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_char_ptr_free_for_next_usage_with_size(dpf_vector, data, sizes, size, modified):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_char_ptr_free(dpf_vector, data, size, modified):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_char_ptr_free_for_next_usage(dpf_vector, data, size, modified):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_double_commit(dpf_vector, data, size, modified):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_int_commit(dpf_vector, data, size, modified):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_char_commit(dpf_vector, data, size, modified):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_char_ptr_commit(dpf_vector, data, size, modified):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_char_ptr_commit_with_size(dpf_vector, data, sizes, size, modified):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_delete(dpf_vector):
		raise NotImplementedError

	@staticmethod
	def dpf_string_free(dpf_vector, data, size):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_duplicate_dpf_vector(dpf_vector):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_double_extract_sub(init_dpf_vector, init_data, init_size, dpf_vector_to_update, first_index, size, data):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_int_extract_sub(init_dpf_vector, init_data, init_size, dpf_vector_to_update, first_index, size, data):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_char_extract_sub(init_dpf_vector, init_data, init_size, dpf_vector_to_update, first_index, size, data):
		raise NotImplementedError

	@staticmethod
	def dpf_vector_new_for_object(api_to_use):
		raise NotImplementedError

	@staticmethod
	def dpf_string_free_for_object(api_to_use, dpf_vector, data, size):
		raise NotImplementedError

