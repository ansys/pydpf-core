#-------------------------------------------------------------------------------
# Support
#-------------------------------------------------------------------------------

class SupportAbstractAPI:
	@staticmethod
	def init_support_environment(object):
		pass

	@staticmethod
	def finish_support_environment(object):
		pass

	@staticmethod
	def support_delete(support):
		raise NotImplementedError

	@staticmethod
	def support_is_domain_mesh_support(support):
		raise NotImplementedError

	@staticmethod
	def support_set_as_domain_mesh_support(support, meshed_region):
		raise NotImplementedError

	@staticmethod
	def support_get_as_meshed_support(support):
		raise NotImplementedError

	@staticmethod
	def support_get_as_cyclic_support(support):
		raise NotImplementedError

	@staticmethod
	def support_get_as_time_freq_support(support):
		raise NotImplementedError

	@staticmethod
	def support_get_field_support_by_property(support, prop_name):
		raise NotImplementedError

	@staticmethod
	def support_get_property_field_support_by_property(support, prop_name):
		raise NotImplementedError

	@staticmethod
	def support_get_string_field_support_by_property(support, prop_name):
		raise NotImplementedError

	@staticmethod
	def support_get_property_names_as_string_coll_for_fields(support):
		raise NotImplementedError

	@staticmethod
	def support_get_property_names_as_string_coll_for_property_fields(support):
		raise NotImplementedError

	@staticmethod
	def support_get_property_names_as_string_coll_for_string_fields(support):
		raise NotImplementedError

