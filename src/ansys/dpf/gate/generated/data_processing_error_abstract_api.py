#-------------------------------------------------------------------------------
# DataProcessingError
#-------------------------------------------------------------------------------

class DataProcessingErrorAbstractAPI:
	@staticmethod
	def init_data_processing_error_environment(object):
		pass

	@staticmethod
	def finish_data_processing_error_environment(object):
		pass

	@staticmethod
	def data_processing_parse_error(size, error_message):
		raise NotImplementedError

	@staticmethod
	def data_processing_parse_error_to_str(size, error_message):
		raise NotImplementedError

	@staticmethod
	def dpf_error_new():
		raise NotImplementedError

	@staticmethod
	def dpf_error_set_throw(error, must_throw):
		raise NotImplementedError

	@staticmethod
	def dpf_error_set_code(error, code_value):
		raise NotImplementedError

	@staticmethod
	def dpf_error_set_message_text(error, code_value):
		raise NotImplementedError

	@staticmethod
	def dpf_error_set_message_template(error, code_value):
		raise NotImplementedError

	@staticmethod
	def dpf_error_set_message_id(error, code_value):
		raise NotImplementedError

	@staticmethod
	def dpf_error_delete(error):
		raise NotImplementedError

	@staticmethod
	def dpf_error_duplicate(error):
		raise NotImplementedError

	@staticmethod
	def dpf_error_code(error):
		raise NotImplementedError

	@staticmethod
	def dpf_error_to_throw(error):
		raise NotImplementedError

	@staticmethod
	def dpf_error_message_text(error):
		raise NotImplementedError

	@staticmethod
	def dpf_error_message_template(error):
		raise NotImplementedError

	@staticmethod
	def dpf_error_message_id(error):
		raise NotImplementedError

	@staticmethod
	def data_processing_parse_error_to_str_for_object(api_to_use, size, error_message):
		raise NotImplementedError

