#-------------------------------------------------------------------------------
# GenericDataContainer
#-------------------------------------------------------------------------------

class GenericDataContainerAbstractAPI:
	@staticmethod
	def init_generic_data_container_environment(object):
		pass

	@staticmethod
	def finish_generic_data_container_environment(object):
		pass

	@staticmethod
	def generic_data_container_new():
		raise NotImplementedError

	@staticmethod
	def generic_data_container_get_property_any(container, name):
		raise NotImplementedError

	@staticmethod
	def generic_data_container_set_property_any(container, name, any):
		raise NotImplementedError

	@staticmethod
	def generic_data_container_set_property_dpf_type(container, name, any):
		raise NotImplementedError

	@staticmethod
	def generic_data_container_get_property_types(container):
		raise NotImplementedError

	@staticmethod
	def generic_data_container_get_property_names(container):
		raise NotImplementedError

	@staticmethod
	def generic_data_container_new_on_client(client):
		raise NotImplementedError

	@staticmethod
	def generic_data_container_get_copy(id, client):
		raise NotImplementedError

