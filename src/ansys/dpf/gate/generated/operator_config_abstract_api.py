#-------------------------------------------------------------------------------
# OperatorConfig
#-------------------------------------------------------------------------------

class OperatorConfigAbstractAPI:
	@staticmethod
	def init_operator_config_environment(object):
		pass

	@staticmethod
	def finish_operator_config_environment(object):
		pass

	@staticmethod
	def operator_config_default_new(op):
		raise NotImplementedError

	@staticmethod
	def operator_config_empty_new():
		raise NotImplementedError

	@staticmethod
	def operator_config_get_int(config, option):
		raise NotImplementedError

	@staticmethod
	def operator_config_get_double(config, option):
		raise NotImplementedError

	@staticmethod
	def operator_config_get_bool(config, option):
		raise NotImplementedError

	@staticmethod
	def operator_config_set_int(config, option, value):
		raise NotImplementedError

	@staticmethod
	def operator_config_set_double(config, option, value):
		raise NotImplementedError

	@staticmethod
	def operator_config_set_bool(config, option, value):
		raise NotImplementedError

	@staticmethod
	def operator_config_get_num_config(config):
		raise NotImplementedError

	@staticmethod
	def operator_config_get_config_option_name(config, index):
		raise NotImplementedError

	@staticmethod
	def operator_config_get_config_option_printable_value(config, index):
		raise NotImplementedError

	@staticmethod
	def operator_config_has_option(config, option):
		raise NotImplementedError

	@staticmethod
	def operator_config_default_new_on_client(client, op):
		raise NotImplementedError

	@staticmethod
	def operator_config_empty_new_on_client(client):
		raise NotImplementedError

