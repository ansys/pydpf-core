#-------------------------------------------------------------------------------
# SpecificationExternalization
#-------------------------------------------------------------------------------

class SpecificationExternalizationAbstractAPI:
	@staticmethod
	def init_specification_externalization_environment(object):
		pass

	@staticmethod
	def finish_specification_externalization_environment(object):
		pass

	@staticmethod
	def specification_xml_export(filepath):
		raise NotImplementedError

	@staticmethod
	def specification_xml_import(filepath):
		raise NotImplementedError

	@staticmethod
	def set_specification_in_core(registry):
		raise NotImplementedError

