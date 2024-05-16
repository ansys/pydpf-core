#-------------------------------------------------------------------------------
# FieldMapping
#-------------------------------------------------------------------------------

class FieldMappingAbstractAPI:
	@staticmethod
	def init_field_mapping_environment(object):
		pass

	@staticmethod
	def finish_field_mapping_environment(object):
		pass

	@staticmethod
	def mapping_delete(obj):
		raise NotImplementedError

	@staticmethod
	def mapping_map(obj, in_field):
		raise NotImplementedError

