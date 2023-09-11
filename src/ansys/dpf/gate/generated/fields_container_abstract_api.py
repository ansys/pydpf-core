#-------------------------------------------------------------------------------
# FieldsContainer
#-------------------------------------------------------------------------------

class FieldsContainerAbstractAPI:
	@staticmethod
	def init_fields_container_environment(object):
		pass

	@staticmethod
	def finish_fields_container_environment(object):
		pass

	@staticmethod
	def fields_container_new():
		raise NotImplementedError

	@staticmethod
	def fields_container_delete(fieldContainer):
		raise NotImplementedError

	@staticmethod
	def fields_container_at(fieldContainer, i, ic):
		raise NotImplementedError

	@staticmethod
	def fields_container_set_field(fieldContainer, field, fieldId, ic):
		raise NotImplementedError

	@staticmethod
	def fields_container_get_scoping(fieldContainer, ic, size):
		raise NotImplementedError

	@staticmethod
	def fields_container_num_fields(fieldContainer):
		raise NotImplementedError

