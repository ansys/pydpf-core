#-------------------------------------------------------------------------------
# GenericSupport
#-------------------------------------------------------------------------------

class GenericSupportAbstractAPI:
	@staticmethod
	def init_generic_support_environment(object):
		pass

	@staticmethod
	def finish_generic_support_environment(object):
		pass

	@staticmethod
	def generic_support_new(name):
		raise NotImplementedError

	@staticmethod
	def generic_support_set_field_support_of_property(support, name, field):
		raise NotImplementedError

	@staticmethod
	def generic_support_set_property_field_support_of_property(support, name, field):
		raise NotImplementedError

	@staticmethod
	def generic_support_set_string_field_support_of_property(support, name, field):
		raise NotImplementedError

	@staticmethod
	def generic_support_new_on_client(client, name):
		raise NotImplementedError

