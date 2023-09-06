#-------------------------------------------------------------------------------
# ExternalData
#-------------------------------------------------------------------------------

class ExternalDataAbstractAPI:
	@staticmethod
	def init_external_data_environment(object):
		pass

	@staticmethod
	def finish_external_data_environment(object):
		pass

	@staticmethod
	def external_data_wrap(external_data, deleter):
		raise NotImplementedError

	@staticmethod
	def external_data_free(var1):
		raise NotImplementedError

	@staticmethod
	def external_data_get(external_data):
		raise NotImplementedError

